"""Locals: the record this module manages."""

from pydantic import BaseModel


class Locals(BaseModel):
    id: int
    name: str
