import os

from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    api_key: str
    mongo_db_url: str
    mongo_db_name: str
    weather_base_url: str = "https://api.openweathermap.org/data/3.0/onecall?"
    geocoding_base_url: str = "http://api.openweathermap.org/geo/1.0/direct?"

    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()
