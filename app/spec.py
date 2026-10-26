"""Spec: the record this module manages."""

from pydantic import BaseModel


class Spec(BaseModel):
    id: int
    name: str
