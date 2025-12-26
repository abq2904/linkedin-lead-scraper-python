# AI-Powered LinkedIn Lead Scraper  

Extract **high-quality B2B leads** from LinkedIn without getting blocked. This script:  
- Scrapes LinkedIn profiles **without API access** (using Selenium)  
- Cleans data with **OpenAI enrichment** (identifies decision-makers)  
- Exports to **CSV/Google Sheets** for sales teams  

👉 **Perfect for**: SaaS companies, recruiters, and agencies needing **targeted lead lists**.  

## 🚀 Key Features  
- **Human-like scraping** (avoids IP bans)  
- **AI enrichment** (extracts emails/company data via OpenAI)  
- **CRM-ready output** (CSV, Airtable, or Google Sheets)  

## ⚠️ Legal Note  
This tool follows LinkedIn's [robots.txt](https://www.linkedin.com/robots.txt) guidelines:  
- **No brute-force scraping** (respects `Crawl-Delay`)  
- **For personal/ethical use only**  

## ⚙️ Tech Stack  
- Python 3.10+  
- Selenium (with undetected-chromedriver)  
- OpenAI API (GPT-4 for data enrichment)  
- Pandas (data cleaning)  


## 🛠️ Installation  
```bash
git clone https://github.com/abq2904/linkedin-lead-scraper-python.git
cd linkedin-lead-scraper-python
pip install -r requirements.txt
```

## 🎯 Usage
python scraper.py --query "CTO at SaaS startups in USA" --pages 5


📊 Output Example
Name	Title	Company	Email
John Doe	CTO @ScaleFast	ScaleFast	johndoe@scalefast.com
💼 Business Use Cases
B2B Lead Generation: Find ideal customers for your SaaS product

Recruitment: Source passive candidates with specific skills

Competitor Analysis: Map org structures of rival companies

📌 Need a custom solution? Send me message
