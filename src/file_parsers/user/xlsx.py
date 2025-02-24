import io
from typing import Generator

import pandas as pd

from core.entities import User

from .dataframe import parse_dataframe


def parse_excel_bytes(content: bytes) -> Generator[User]:
    df = pd.read_excel(io.BytesIO(content))
    return parse_dataframe(df)
