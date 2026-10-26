"""Proxy: the record this module manages."""

from pydantic import BaseModel


class Proxy(BaseModel):
    id: int
    name: str
