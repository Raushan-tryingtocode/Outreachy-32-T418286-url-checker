""" 
This script reads URLs from a CSV file and prints their HTTP status codes.
"""
import csv
import requests


def check_url(file_path):
    """ The main funtion to read the URL's and print the status code for each URL"""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue

            url = row[0]

            try:
                response = requests.get(url, timeout=5)
                print(f"({response.status_code}) {url}")
            except requests.exceptions.RequestException:
                print(f"(Error) {url}")


if __name__ == "__main__":
    check_url('Task 2 - Intern.csv')
