from pydantic_settings import BaseSettings, SettingsConfigDict


class TwilioSettings(BaseSettings):
    ACCOUNT_SID: str
    AUTH_TOKEN: str
    PHONE_NUMBER: str

    model_config = SettingsConfigDict(env_file=".env")
