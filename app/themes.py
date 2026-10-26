"""Themes: the record this module manages."""

from pydantic import BaseModel


class Themes(BaseModel):
    id: int
    name: str
