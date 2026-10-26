"""Changesets: the record this module manages."""

from pydantic import BaseModel


class Changesets(BaseModel):
    id: int
    name: str
