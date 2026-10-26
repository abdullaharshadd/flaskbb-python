"""Tokens: the record this module manages."""

from pydantic import BaseModel


class Tokens(BaseModel):
    id: int
    name: str
