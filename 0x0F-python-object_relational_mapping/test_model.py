#!/usr/bin/python3
"""
using the SQLAlchemy ORM module
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128))
