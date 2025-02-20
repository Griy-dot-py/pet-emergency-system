from pydantic import BaseModel


class GroupSchema(BaseModel):
    member_ids: list[int]
    name: str
    message: str
