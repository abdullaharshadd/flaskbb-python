"""Verifiers: the record this module manages."""

from pydantic import BaseModel


class Verifiers(BaseModel):
    id: int
    name: str
