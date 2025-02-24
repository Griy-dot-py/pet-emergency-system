from email.message import EmailMessage

import aiosmtplib

import services
from config import SMTPSettings

config = SMTPSettings()


async def send(message: EmailMessage):
    message["From"] = config.SMTP_ADDRESS
    return await aiosmtplib.send(
        message, hostname=config.SMTP_HOST, port=config.SMTP_PORT
    )


email_service = services.SMTPEmailService(sender=send)
