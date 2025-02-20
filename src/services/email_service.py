from dataclasses import dataclass
from email.message import EmailMessage

import aiosmtplib

from notificator import NotificationEvent, NotificationService


@dataclass
class SMTPEmailService(NotificationService):
    host: str
    port: int
    email_address: str

    async def __call__(self, event: NotificationEvent):
        message = EmailMessage()
        message["From"] = self.email_address
        message["To"] = event.address
        message["Subject"] = "Notification"
        message.set_content(event.message)

        await aiosmtplib.send(message, hostname=self.host, port=self.port)
