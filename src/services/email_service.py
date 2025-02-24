from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from email.message import EmailMessage

from notificator import NotificationEvent, NotificationService

# import aiosmtplib



@dataclass
class SMTPEmailService(NotificationService):
    # host: str
    # port: int
    # email_address: str
    sender: Callable[[EmailMessage], Awaitable[None]]

    async def __call__(self, event: NotificationEvent):
        message = EmailMessage()
        # message["From"] = self.email_address
        message["To"] = event.address
        message["Subject"] = "Notification"
        message.set_content(event.message)

        await self.sender(message)
        # await aiosmtplib.send(message, hostname=self.host, port=self.port)
