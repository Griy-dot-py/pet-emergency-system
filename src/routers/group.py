from core.entities import Group

from .cutom import CustomRouter
from .schemas import GroupSchema


class GroupRouter(CustomRouter):
    def compile(self):
        self.fastapi_router.add_route(self.fastapi_router.prefix, self.post, methods=["POST"])

    async def post(self, body: GroupSchema) -> int:
        new = Group(**body.model_dump())
        id = await self.core.create_group(new)
        return id
