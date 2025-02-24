from twilio.http.async_http_client import AsyncTwilioHttpClient  # type: ignore
from twilio.rest import Client  # type: ignore

import services
from config import TwilioSettings

config = TwilioSettings()

http_cli = AsyncTwilioHttpClient()
cli = Client(config.ACCOUNT_SID, config.AUTH_TOKEN, http_client=http_cli)

sms_service = services.TwilioSMSService(client=cli, phone_number=config.PHONE_NUMBER)
