"""Models for the BCV API."""

from sqlalchemy import Boolean, Column, Integer, String, Date, Float

from bcv_api.database import Base

class Rate(Base):
    """Rate model."""

    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    dollar = Column(Float)
    date = Column(Date, index=True, default=Date())
