"""Plugins: the record this module manages."""

from pydantic import BaseModel


class Plugins(BaseModel):
    id: int
    name: str
