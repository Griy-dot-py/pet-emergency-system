from typing import Annotated

from fastapi import File

from file_parsers import user

from .cutom import CustomRouter


class UserBulkRouter(CustomRouter):
    prefix = "/user/bulk"

    def __init__(self):
        super().__init__()
        self.__router.add_route("/csv", self.post_csv, methods=["POST"])
        self.__router.add_route("/xlsx", self.post_excel, methods=["POST"])

    async def post_csv(self, file: Annotated[bytes, File()]) -> list[int]:
        parser = user.parse_csv_bytes(file)
        return await self.core.add_users(parser)

    async def post_excel(self, file: Annotated[bytes, File()]) -> list[int]:
        parser = user.parse_excel_bytes(file)
        return await self.core.add_users(parser)
