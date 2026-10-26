"""Permissions: the record this module manages."""

from pydantic import BaseModel


class Permissions(BaseModel):
    id: int
    name: str
