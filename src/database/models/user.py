from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .contact import Contact


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    contacts: Mapped[list[Contact]] = relationship(lazy="joined")
