"""Database: the record this module manages."""

from pydantic import BaseModel


class Database(BaseModel):
    id: int
    name: str
