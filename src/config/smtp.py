from pydantic_settings import BaseSettings, SettingsConfigDict


class SMTPSettings(BaseSettings):
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_ADDRESS: str

    model_config = SettingsConfigDict(env_file=".env")
