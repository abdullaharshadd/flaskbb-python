"""Helpers: the record this module manages."""

from pydantic import BaseModel


class Helpers(BaseModel):
    id: int
    name: str
