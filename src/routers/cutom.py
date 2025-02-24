from abc import ABC, abstractmethod
from dataclasses import dataclass

from fastapi import APIRouter

from core import ENS


@dataclass
class CustomRouter(ABC):
    core: ENS
    fastapi_router: APIRouter

    @abstractmethod
    def compile(self) -> None: ...
