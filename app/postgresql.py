"""Postgresql: the record this module manages."""

from pydantic import BaseModel


class Postgresql(BaseModel):
    id: int
    name: str
