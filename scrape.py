#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# Example site (use a public page for demo)
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Print the first 3 links as a simple test
for link in soup.find_all("a")[:3]:
    print(link.get_text(), link.get("href"))