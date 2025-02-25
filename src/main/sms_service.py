from twilio.http.async_http_client import AsyncTwilioHttpClient  # type: ignore
from twilio.rest import Client  # type: ignore

import services
from config import settings as config

http_cli = AsyncTwilioHttpClient()
cli = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, http_client=http_cli)

sms_service = services.TwilioSMSService(client=cli, phone_number=config.TWILIO_PHONE_NUMBER)
