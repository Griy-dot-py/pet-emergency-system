from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_DIALECT: str
    DB_DRIVER: str
    DB_MIGRATION_DRIVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_ADDRESS: str

    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
