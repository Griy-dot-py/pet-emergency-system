from dataclasses import dataclass


@dataclass
class Group:
    member_ids: list[int]
    name: str
    message: str
