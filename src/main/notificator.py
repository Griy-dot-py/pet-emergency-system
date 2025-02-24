from notificator import AsyncNotificator

from .email_service import email_service
from .sms_service import sms_service

notificator = AsyncNotificator(
    services={
        "email": email_service,
        "sms": sms_service,
    }
)
