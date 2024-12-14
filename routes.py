from fastapi import APIRouter, HTTPException
from api.scraper import scrape_prices, scrape_reviews
from models.database import save_scraped_data

router = APIRouter()

@router.get("/scrape-prices/")
async def scrape_prices_endpoint(url: str):
    data = scrape_prices(url)
    save_scraped_data(data)
    return {"status": "success", "data": data}

@router.get("/scrape-reviews/")
async def scrape_reviews_endpoint(url: str):
    data = scrape_reviews(url)
    save_scraped_data(data)
    return {"status": "success", "data": data}


---