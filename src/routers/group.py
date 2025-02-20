from core.entities import Group

from .cutom import CustomRouter
from .schemas import GroupSchema


class GroupRouter(CustomRouter):
    prefix = "/group"

    def __init__(self):
        super().__init__()
        self.__router.add_route("", self.post, methods=["POST"])

    async def post(self, body: GroupSchema) -> int:
        new = Group(**body.model_dump())
        id = await self.core.create_group(new)
        return id
