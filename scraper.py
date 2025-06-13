### **🛠️ Code (scraper.py)**  
```python
import time
import random
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome, ChromeOptions
import pandas as pd
import openai

# Load config
config = configparser.ConfigParser()
config.read('config.ini')

# Set up Selenium
options = ChromeOptions()
options.add_argument("--headless")  # Run in background
driver = Chrome(options=options)

def login_to_linkedin():
    driver.get("https://www.linkedin.com/login")
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.ID, "username").send_keys(config['linkedin']['email'])
    driver.find_element(By.ID, "password").send_keys(config['linkedin']['password'])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(random.uniform(2, 5))

def scrape_profiles(search_query, pages=3):
    profiles = []
    for page in range(1, pages + 1):
        url = f"https://www.linkedin.com/search/results/people/?keywords={search_query}&page={page}"
        driver.get(url)
        time.sleep(random.uniform(3, 7))  # Human-like delay
        
        # Extract profile data
        for element in driver.find_elements(By.CLASS_NAME, "entity-result__item"):
            name = element.find_element(By.CLASS_NAME, "entity-result__title-text").text
            title = element.find_element(By.CLASS_NAME, "entity-result__primary-subtitle").text
            company = element.find_element(By.CLASS_NAME, "entity-result__secondary-subtitle").text
            profiles.append({"Name": name, "Title": title, "Company": company})
    
    return pd.DataFrame(profiles)

def enrich_with_openai(df):
    openai.api_key = config['openai']['api_key']
    for idx, row in df.iterrows():
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": f"Predict the email of {row['Name']} at {row['Company']} in format firstname.lastname@company.com"
            }]
        )
        df.at[idx, 'Email'] = response.choices[0].message.content
    return df

if __name__ == "__main__":
    login_to_linkedin()
    df = scrape_profiles("CTO at SaaS startups", pages=2)
    df = enrich_with_openai(df)
    df.to_csv("leads.csv", index=False)
    driver.quit()
