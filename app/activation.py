"""Activation: the record this module manages."""

from pydantic import BaseModel


class Activation(BaseModel):
    id: int
    name: str
