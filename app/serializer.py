"""Serializer: the record this module manages."""

from pydantic import BaseModel


class Serializer(BaseModel):
    id: int
    name: str
