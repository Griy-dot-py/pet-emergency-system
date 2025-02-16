from dataclasses import dataclass

from .contact import Contact


@dataclass
class User:
    name: str
    contacts: list[Contact]
