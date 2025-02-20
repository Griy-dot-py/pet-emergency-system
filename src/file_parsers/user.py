from abc import ABC, abstractmethod
from typing import Iterable, Iterator

from core.entities import User


class _UserFileParser(Iterable, ABC):
    @abstractmethod
    def __iter__(self) -> Iterator[User]: ...
