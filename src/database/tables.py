from sqlalchemy import Column, ForeignKey, Table

from .models import Base

group_to_user = Table(
    "group2user",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("group_id", ForeignKey("group.id"), primary_key=True),
)
