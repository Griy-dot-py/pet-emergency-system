from .cutom import CustomRouter


class NotificationRouter(CustomRouter):
    def compile(self):
        self.fastapi_router.post("")(self.post)

    async def post(self, group_id: int) -> None:
        await self.core.notify_group(group_id)
