import requests
from bs4 import BeautifulSoup

url = input("Enter URL to scrape: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("Page Title:", soup.title.string if soup.title else "No title")
