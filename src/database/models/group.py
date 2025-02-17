from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


class Group(Base):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    message: Mapped[str]

    members: Mapped[list[User]] = relationship(secondary="group2user", lazy="joined")
