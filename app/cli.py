"""Cli: the record this module manages."""

from pydantic import BaseModel


class Cli(BaseModel):
    id: int
    name: str
