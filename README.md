# Outreachy-32-T418286: URL Status Checker

This project is a Python-based utility developed as a micro-task for Outreachy. The script reads a list of URLs from a CSV file and verifies their availability by printing their HTTP status codes.

## Features
- **CSV Processing:** Automatically reads URLs from a specified CSV file.
- **Robust Error Handling:** Uses `try-except` blocks to handle network timeouts, DNS errors, and connection issues without crashing the script.
- **Clean Output:** Outputs status codes in the format `(STATUS CODE) URL` as requested.
- **Efficiency:** Uses a `5-second` timeout to ensure the script does not hang on unresponsive servers.

## Prerequisites
- **Python 3.x**
- **pip** (Python package installer)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Raushan-tryingtocode/Outreachy-32-T418286-url-checker.git](https://github.com/Raushan-tryingtocode/Outreachy-32-T418286-url-checker.git)
   cd Outreachy-32-T418286-url-checker
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3.**Usage:**
* Place your CSV file in the project directory.
* Update the filename in url_checker.py if necessary:
  ```bash
  check_url('your_file_name.csv')
           
* Run the script:
  ```bash
  python url_checker.py

## Contribution

This script was created to address the T418286 wishlist proposal for Lusophone technological projects.
