# extractor.py

import re

def extract_emails(text):
    """Returns a list of all email addresses found in the input text."""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def save_emails(emails, filename="emails_found.txt"):
    """Saves extracted emails into a text file."""
    with open(filename, "w") as f:
        f.write("Extracted Emails:\n")
        f.write("=================\n\n")
        for email in emails:
            f.write(email + "\n")
