import datetime

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


def _get_date():
    return datetime.datetime.now()


class Notice(BaseModel):
    __tablename__ = 'notices'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    url = Column(String(100))
    content = Column(Text)
    published_time = Column(String(30), default=str(_get_date()))
    Saved_time = Column(String(30), default=str(_get_date()))
    source = Column(String(30))
    publisher = Column(String(30))
