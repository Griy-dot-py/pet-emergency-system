from abc import ABC, abstractmethod
from typing import Iterable

from .entities import Group, User


class Database(ABC):
    @abstractmethod
    async def add_users(self, users: Iterable[User]) -> list[int]: ...

    @abstractmethod
    async def add_group(self, group: Group) -> int: ...

    @abstractmethod
    async def get_group(self, id: int) -> tuple[Group, list[User]] | None: ...
