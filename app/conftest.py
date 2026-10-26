"""Conftest: the record this module manages."""

from pydantic import BaseModel


class Conftest(BaseModel):
    id: int
    name: str
