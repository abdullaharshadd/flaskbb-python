"""Alembic: the record this module manages."""

from pydantic import BaseModel


class Alembic(BaseModel):
    id: int
    name: str
