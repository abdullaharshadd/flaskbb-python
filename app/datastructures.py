"""Datastructures: the record this module manages."""

from pydantic import BaseModel


class Datastructures(BaseModel):
    id: int
    name: str
