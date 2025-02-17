from dataclasses import dataclass

import aiosmtplib
from email.message import EmailMessage

from notificator import NotificationService, NotificationEvent


@dataclass
class SMTPService(NotificationService):
    host: str
    port: int
    address: str

    async def __call__(self, event: NotificationEvent):
        message = EmailMessage()
        message["From"] = self.address
        message["To"] = event.address
        message["Subject"] = "Notification"
        message.set_content(event.message)
        
        await aiosmtplib.send(message, hostname=self.host, port=self.port)
