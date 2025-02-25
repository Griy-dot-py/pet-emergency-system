from sqlalchemy.ext.asyncio import create_async_engine

from config import settings as config
from database import SQLAlchemyDB

SQLA_PATTERN = "{dialect}+{driver}://{user}:{password}@{host}:{port}/{db}"

url = SQLA_PATTERN.format(
    dialect=config.DB_DIALECT,
    driver=config.DB_DRIVER,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    db=config.DB_NAME,
)
db = SQLAlchemyDB(create_async_engine(url))
