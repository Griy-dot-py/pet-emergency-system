from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    DB_DIALECT: str
    DB_DRIVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=".env")
