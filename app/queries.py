"""Queries: the record this module manages."""

from pydantic import BaseModel


class Queries(BaseModel):
    id: int
    name: str
