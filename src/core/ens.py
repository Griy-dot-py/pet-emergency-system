from typing import Iterable

from .db import Database
from .entities import Group, User
from .notificator import Notificator


class ENS:
    def __init__(self, db: Database, notificator: Notificator) -> None:
        self.__db = db
        self.__notificator = notificator

    async def add_users(self, users: Iterable[User]) -> list[int]:
        return await self.__db.add_users(users)

    async def create_group(self, group: Group) -> int:
        return await self.__db.add_group(group)

    async def notify_group(self, group_id: int) -> None:
        result = await self.__db.get_group(group_id)
        if result is not None:
            group, members = result
            for member in members:
                for contact in member.contacts:
                    await self.__notificator(contact, group.message)
