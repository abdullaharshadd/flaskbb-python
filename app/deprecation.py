"""Deprecation: the record this module manages."""

from pydantic import BaseModel


class Deprecation(BaseModel):
    id: int
    name: str
