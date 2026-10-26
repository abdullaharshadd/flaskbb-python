"""Reauthentication: the record this module manages."""

from pydantic import BaseModel


class Reauthentication(BaseModel):
    id: int
    name: str
