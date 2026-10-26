"""Definitions: the record this module manages."""

from pydantic import BaseModel


class Definitions(BaseModel):
    id: int
    name: str
