"""Exceptions: the record this module manages."""

from pydantic import BaseModel


class Exceptions(BaseModel):
    id: int
    name: str
