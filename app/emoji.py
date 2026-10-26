"""Emoji: the record this module manages."""

from pydantic import BaseModel


class Emoji(BaseModel):
    id: int
    name: str
