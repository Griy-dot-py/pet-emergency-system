from abc import ABC
from dataclasses import dataclass

from fastapi import APIRouter

from core import ENS


@dataclass
class CustomRouter(ABC):
    core: ENS
    prefix: str

    def compile(self) -> APIRouter:
        return self.__router

    def __init__(self):
        self.__router = APIRouter(self.prefix)
