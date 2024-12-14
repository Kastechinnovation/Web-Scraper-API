import requests
from bs4 import BeautifulSoup

def scrape_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Example selectors (customize for each platform)
    title = soup.select_one("h1.product-title").text.strip()
    price = soup.select_one(".price-tag").text.strip()
    return {"title": title, "price": price, "url": url}

def scrape_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    reviews = [review.text.strip() for review in soup.select(".review-text")]
    return {"reviews": reviews, "url": url}


---