from core import ENS

from .db import db
from .notificator import notificator

ens = ENS(db=db, notificator=notificator)
