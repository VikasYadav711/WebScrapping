#pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup


# iii.
base_url = "http://quotes.toscrape.com"
next_page_url = "/page/1/"  # Start from page 1

while next_page_url:
    # Build the full URL for each page
    full_url = base_url + next_page_url
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract quotes on the current page
    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        print(f"{text} — {author}")

    # Find the 'Next' page link
    next_btn = soup.select_one("li.next a")
    if next_btn:
        next_page_url = next_btn["href"]
    else:
        next_page_url = None  # No more pages





""" Multi Line comments before iii. till we've done the work earlier


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

    """