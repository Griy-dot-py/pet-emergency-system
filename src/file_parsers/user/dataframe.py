# import re
# import string
from typing import Generator

import pandas as pd

from core.entities import Contact, User


def parse_dataframe(df: pd.DataFrame) -> Generator[User]:
    for i, row in df.iterrows():
        contacts = [
            Contact(
                # service=re.match(f"[{string.ascii_letters}]+", col).group(),
                service=col.split(".")[0],
                address=row[col],
            )
            for col in df.columns[1:]
            if row[col] is not None
        ]
        yield User(name=row["name"], contacts=contacts)
