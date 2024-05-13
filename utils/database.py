from sqlalchemy import Column, INTEGER
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import SETTINGS


class Base(DeclarativeBase):
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    engine = create_async_engine(SETTINGS.DATABASE_URL.replace('sqlite:///', 'sqlite+aiosqlite:///'))
    session = async_sessionmaker(bind=engine)
    
    
    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')