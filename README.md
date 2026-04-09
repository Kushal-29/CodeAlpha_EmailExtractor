📧 CodeAlpha Email Extractor

A Python tool that automates the extraction of email addresses from websites and text sources using URL crawling and pattern matching.

Extract emails quickly and reliably from webpages using advanced regex and scraping techniques — ideal for data collection, lead generation, or text analysis.

🧠 Project Overview

In many real-world applications — like market research, automated data gathering, or contact discovery — extracting email addresses programmatically is essential. This project builds a simple yet powerful email extraction utility that:

✔ Crawls websites
✔ Extracts all email addresses found
✔ Stores them in structured output
✔ Works both from URLs and text input
   
🚀 Key Features.  
    
✔ Extract email addresses from any URL
✔ Supports single page and multi-page crawling
✔ Regex-based accurate email matching
✔ Outputs to CSV for easy use in spreadsheets
✔ Lightweight and easy to run

📦 Tech Stack
Layer	Tools / Libraries
Language	Python
Web Requests	requests
HTML Parsing	BeautifulSoup
Pattern Matching	Regular Expressions (re)
Output	CSV
📁 Project Structure
CodeAlpha_EmailExtractor/
│
├── extractor.py             # Main email extraction script
├── output/                  # Folder where extracted results save
│   └── emails.csv
├── requirements.txt         # Dependencies
└── README.md

🧪 How It Works

User provides a URL or text input

The script fetches the web page content

BeautifulSoup parses HTML

Regex scans for email patterns

Emails are extracted and cleaned

Results are saved to emails.csv

📥 Installation & Setup
Step 1 — Clone the Repository
git clone https://github.com/Kushal-29/CodeAlpha_EmailExtractor.git
cd CodeAlpha_EmailExtractor

Step 2 — Create Virtual Environment (recommended)
python-m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

Step 3 — Install Dependencies
pip install -r requirements.txt

🚀 How to Use
🔹 Run from Terminal
python extractor.py

🔹 Enter a URL or provide a text file

Example:

Enter URL: https://example.com


The script will:
✔ Fetch the page
✔ Extract email addresses
✔ Save them into output/emails.csv
