"""Populate: the record this module manages."""

from pydantic import BaseModel


class Populate(BaseModel):
    id: int
    name: str
