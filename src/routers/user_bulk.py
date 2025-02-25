from typing import Annotated

from fastapi import File

from file_parsers import user

from .cutom import CustomRouter


class UserBulkRouter(CustomRouter):
    def compile(self):
        self.fastapi_router.post("/csv")(self.post_csv)
        self.fastapi_router.post("/excel")(self.post_excel)
    async def post_csv(self, file: Annotated[bytes, File()]) -> list[int]:
        parser = user.parse_csv_bytes(file)
        return await self.core.add_users(parser)

    async def post_excel(self, file: Annotated[bytes, File()]) -> list[int]:
        parser = user.parse_excel_bytes(file)
        return await self.core.add_users(parser)
