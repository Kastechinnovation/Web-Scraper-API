from apscheduler.schedulers.background import BackgroundScheduler
from utils.notifications import send_email
from api.scraper import scrape_prices

scheduler = BackgroundScheduler()

def schedule_price_scraping(url, email):
    data = scrape_prices(url)
    send_email(email, "Price Scraping Result", str(data))
    return data

# Example Task
scheduler.add_job(schedule_price_scraping, "interval", minutes=60, args=["https://example.com", "user@example.com"])

scheduler.start()