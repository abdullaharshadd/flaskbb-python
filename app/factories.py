"""Factories: the record this module manages."""

from pydantic import BaseModel


class Factories(BaseModel):
    id: int
    name: str
