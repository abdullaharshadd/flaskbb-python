"""Conf: the record this module manages."""

from pydantic import BaseModel


class Conf(BaseModel):
    id: int
    name: str
