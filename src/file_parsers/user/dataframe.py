from typing import Iterator
import re

import string
from core.entities import User, Contact

import pandas as pd


def parse_dataframe(df: pd.DataFrame) -> Iterator[User]:
    for row in df.iterrows():
        contacts = [Contact(service=re.match(f"[{string.ascii_letters}]+", col).group(), address=row[col]) for col in df.columns[1:] if row[col] is not None]
        yield User(name=row["name"], contacts=contacts)
