"""Wsgi: the record this module manages."""

from pydantic import BaseModel


class Wsgi(BaseModel):
    id: int
    name: str
