from .dataframe import parse_dataframe
from typing import Iterator
from core.entities import User
import pandas as pd
import io


def parse_excel_bytes(content: bytes) -> Iterator[User]:
    df = pd.read_excel(io.BytesIO(content))
    return parse_dataframe(df)
