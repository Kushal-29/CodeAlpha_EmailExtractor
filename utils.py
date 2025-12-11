# utils.py

def read_file(filepath):
    """Reads and returns content from a file."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("❌ File not found! Please check the file path.")
        return None
