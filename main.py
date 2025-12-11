# main.py

from utils import read_file
from extractor import extract_emails, save_emails

def main():
    print("📧 Email Extractor Automation Tool")
    print("Reads a text file and extracts all email addresses.\n")

    filepath = input("Enter the path of the text file (e.g., sample.txt): ").strip()
    content = read_file(filepath)

    if content is None:
        return

    emails = extract_emails(content)

    if emails:
        print(f"\n✔️ Found {len(emails)} email(s):")
        for e in emails:
            print("→", e)

        save = input("\nSave results to 'emails_found.txt'? (y/n): ").lower()
        if save == "y":
            save_emails(emails)
            print("📁 Saved to emails_found.txt")
    else:
        print("\n⚠️ No email addresses found in the file.")

    print("\nDone!")

if __name__ == "__main__":
    main()
