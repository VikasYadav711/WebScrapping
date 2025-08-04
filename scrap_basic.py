#pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())  # View the HTML content . Commented when putting ii. 

# ii.

for quote in soup.select(".quote"):
    text = quote.select_one(".text").get_text(strip=True)
    author = quote.select_one(".author").get_text(strip=True)
    print(f"{text} — {author}")