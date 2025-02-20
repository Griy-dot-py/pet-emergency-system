import csv
from typing import Iterable

from .user import _UserFileParser


class UserCSVParser(_UserFileParser):
    def __init__(self, file: Iterable[str]):
        self.__reader = csv.reader(file)
