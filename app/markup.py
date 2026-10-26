"""Markup: the record this module manages."""

from pydantic import BaseModel


class Markup(BaseModel):
    id: int
    name: str
