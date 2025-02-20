from dataclasses import dataclass

from twilio.http.async_http_client import AsyncTwilioHttpClient  # type: ignore
from twilio.rest import Client  # type: ignore

from notificator import NotificationEvent, NotificationService


@dataclass
class TwilioSMSService(NotificationService):
    account_sid: str
    auth_token: str
    phone_number: str

    def __init__(self):
        http_client = AsyncTwilioHttpClient()
        self.__client = Client(
            self.account_sid, self.auth_token, http_client=http_client
        )

    async def __call__(self, event: NotificationEvent) -> None:
        await self.__client.messages.create_async(
            to=event.address, from_=self.phone_number, body=event.message
        )
