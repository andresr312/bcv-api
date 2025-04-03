"""Depends module for FastAPI application."""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from bcv_api import schemas, services
from bcv_api.config import settings
from bcv_api.database import SessionLocal


def get_db():
    """Get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
