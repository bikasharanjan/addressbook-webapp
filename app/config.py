from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os

class Settings(BaseSettings):
    database_url: str

    class Config:
        # Always load this exact .env file
        env_file = str(Path(__file__).resolve().parent.parent / ".env")

# Load .env manually before creating settings instance
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# Debug check
print("DEBUG >> DATABASE_URL in env:", os.getenv("DATABASE_URL"))

settings = Settings()
