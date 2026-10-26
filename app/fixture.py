"""Fixture: the record this module manages."""

from pydantic import BaseModel


class Fixture(BaseModel):
    id: int
    name: str
