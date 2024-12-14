from fastapi import FastAPI
from api.routes import router
from utils.config import settings
import uvicorn

app = FastAPI(title="Web Scraper API for Business Challenges")

# Include routes
app.include_router(router)

# Run app
if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)


---