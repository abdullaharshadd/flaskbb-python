"""Translations: the record this module manages."""

from pydantic import BaseModel


class Translations(BaseModel):
    id: int
    name: str
