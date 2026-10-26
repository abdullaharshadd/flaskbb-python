"""Sql: the record this module manages."""

from pydantic import BaseModel


class Sql(BaseModel):
    id: int
    name: str
