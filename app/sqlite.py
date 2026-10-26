"""Sqlite: the record this module manages."""

from pydantic import BaseModel


class Sqlite(BaseModel):
    id: int
    name: str
