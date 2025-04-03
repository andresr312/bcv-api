"""Services for the BCV API."""

from datetime import date, timedelta
from typing import List

from sqlalchemy.orm import Session

from bcv_api import models, schemas
from bcv_api.config import settings

# RATE SERVICES


def get_rate(db: Session) -> models.Rate:
    """Get the last rate from the database.

    Parameters:
    ----------
    db: Session
        Database session.

    Returns:
    -------
    models.Rate
    """
    return db.query(models.Rate).order_by(models.Rate.date.desc()).first()


def get_rate_from_date(db: Session, rate_date: date) -> models.Rate:
    """Get the rate from the database for a specific date.

    Parameters:
    ----------
    db: Session
        Database session.
    rate_date: date
        Rate date.

    Returns:
    -------
    models.Rate
    """
    return (
        db.query(models.Rate)
        .filter(models.Rate.date == rate_date)
        .order_by(models.Rate.id.desc())
        .first()
    )


def get_rates(db: Session, skip: int = 0, limit: int = 100) -> List[models.Rate]:
    """Get all rates from the database.

    Parameters:
    ----------
    db: Session
        Database session.
    skip: int
        Number of records to skip.
    limit: int
        Number of records to return.

    Returns:
    -------
    List[models.Rate]
    """
    return db.query(models.Rate).offset(skip).limit(limit).all()


def create_rate(db: Session, rate: schemas.Rate) -> models.Rate:
    """Create a new rate in the database.

    Parameters:
    ----------
    db: Session
        Database session.
    rate: schemas.Rate
        Rate to create.

    Returns:
    -------
    models.Rate
    """
    db_rate = get_rate_from_date(db, rate.date)
    if db_rate:
        return update_rate(db, rate)
    db_rate = models.Rate(dollar=rate.dollar, date=rate.date)
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate


def update_rate(db: Session, rate: schemas.Rate) -> models.Rate:
    """Update a rate in the database.

    Parameters:
    ----------
    db: Session
        Database session.
    rate: schemas.Rate
        Rate to update.

    Returns:
    -------
    models.Rate
    """
    db_rate = get_rate_from_date(db, rate.date)
    if db_rate:
        db_rate.dollar = rate.dollar
        db.commit()
        db.refresh(db_rate)
    return db_rate
