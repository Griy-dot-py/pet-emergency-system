from abc import ABC, abstractmethod

from .event import NotificationEvent


class NotificationService(ABC):
    @abstractmethod
    async def __call__(self, event: NotificationEvent) -> None: ...
