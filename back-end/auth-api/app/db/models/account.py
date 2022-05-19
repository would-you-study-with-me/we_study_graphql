from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP

from app.db.database import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    age = Column(Integer)

