from .cutom import CustomRouter


class NotificationRouter(CustomRouter):
    def compile(self):
        self.fastapi_router.add_route(self.fastapi_router.prefix, self.post, methods=["POST"])

    async def post(self, group_id: int) -> None:
        await self.core.notify_group(group_id)
