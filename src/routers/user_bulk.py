from abc import abstractmethod

from fastapi import UploadFile

from .cutom import CustomRouter


class UserBulkRouter(CustomRouter):
    prefix = "/user/bulk"

    def __init__(self):
        super().__init__()
        self.__router.add_route("/csv", self.post_csv, methods=["POST"])
        self.__router.add_route("/xlsx", self.post_xlsx, methods=["POST"])

    @abstractmethod
    async def post_csv(self, file: UploadFile) -> list[int]: ...

    @abstractmethod
    async def post_xlsx(self, file: UploadFile) -> list[int]: ...
