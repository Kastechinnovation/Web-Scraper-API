from pydantic import BaseSettings

class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    DATABASE_URL: str
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings


---