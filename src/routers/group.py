from core.entities import Group

from .cutom import CustomRouter
from .schemas import GroupSchema


class GroupRouter(CustomRouter):
    def compile(self):
        self.fastapi_router.post("")(self.post)
    async def post(self, body: GroupSchema) -> int:
        new = Group(**body.model_dump())
        id = await self.core.create_group(new)
        return id
