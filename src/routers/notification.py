from .cutom import CustomRouter


class NotificationRouter(CustomRouter):
    def compile(self):
        super().__init__()
        self.__router.add_route("", self.post, methods=["POST"])

    async def post(self, group_id: int) -> None:
        await self.core.notify_group(group_id)
