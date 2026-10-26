"""Proxies: the record this module manages."""

from pydantic import BaseModel


class Proxies(BaseModel):
    id: int
    name: str
