from .dataframe import parse_dataframe
from typing import Iterator
from core.entities import User
import pandas as pd
import io


def parse_csv_bytes(content: bytes) -> Iterator[User]:
    df = pd.read_csv(io.BytesIO(content))
    return parse_dataframe(df)
