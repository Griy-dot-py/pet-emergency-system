from core import Notificator
from core.entities import Contact

from .event import NotificationEvent
from .service import NotificationService


class AsyncNotificator(Notificator):
    def __init__(self, services: dict[str, NotificationService]):
        self.__services = services

    async def __call__(self, contact: Contact, message: str) -> None:
        event = NotificationEvent(contact.address, message)
        await self.__services[contact.service](event)
