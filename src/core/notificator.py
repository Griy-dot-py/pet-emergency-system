from abc import ABC, abstractmethod

from .entities import Contact


class Notificator(ABC):
    @abstractmethod
    async def __call__(self, contact: Contact, message: str) -> None: ...
