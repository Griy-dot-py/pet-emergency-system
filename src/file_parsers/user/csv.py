import io
from typing import Generator

import pandas as pd

from core.entities import User

from .dataframe import parse_dataframe


def parse_csv_bytes(content: bytes) -> Generator[User]:
    df = pd.read_csv(io.BytesIO(content))
    return parse_dataframe(df)
