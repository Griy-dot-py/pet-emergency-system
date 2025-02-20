from dataclasses import asdict
from itertools import chain
from typing import Iterable

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from core import Database
from core.entities import Contact, Group, User

from . import models
from .tables import group_to_user


class SQLAlchemyDB(Database):
    def __init__(self, engine: AsyncEngine):
        self.__sessionmaker = async_sessionmaker(bind=engine)

    async def add_users(self, users: Iterable[User]) -> list[int]:
        async with self.__sessionmaker() as session:
            async with session.begin():
                user_models = [models.User(name=user.name) for user in users]
                session.add_all(user_models)
                await session.flush()

                contacts = (
                    (
                        dict(**asdict(contact), owner_id=model.id)
                        for contact in user.contacts
                    )
                    for user, model in zip(users, user_models)
                )
                await session.execute(
                    insert(models.Contact), [contact for contact in chain(*contacts)]
                )

                return [user.id for user in user_models]
                # for user in users:
                #     session.add(modeller.create_user(user))
                #     await session.flush()
                #     contacts = [modeller.create_contact(contact, user.id) for contact in user.contacts]
                #     session.add_all(contacts)
                #     await session.flush()
                #     ids.append(user.id)

    async def add_group(self, group: Group) -> int:
        async with self.__sessionmaker() as session:
            async with session.begin():
                model = models.Group(name=group.name, message=group.message)
                session.add(model)
                await session.flush()

                await session.execute(
                    insert(group_to_user),
                    [
                        {"user_id": user_id, "group_id": model.id}
                        for user_id in group.member_ids
                    ],
                )

                return model.id

    @staticmethod
    def __create_group(model: models.Group) -> tuple[Group, list[User]]:
        group = Group(
            name=model.name,
            message=model.message,
            member_ids=[user.id for user in model.members],
        )
        users = [
            User(
                name=user.name,
                contacts=[
                    Contact(service=contact.service, address=contact.address)
                    for contact in user.contacts
                ],
            )
            for user in model.members
        ]
        return group, users

    async def get_group(self, id: int) -> tuple[Group, list[User]] | None:
        async with self.__sessionmaker() as session:
            group_model = await session.get(models.Group, id)
            if group_model is None:
                return None
            return self.__create_group(group_model)
