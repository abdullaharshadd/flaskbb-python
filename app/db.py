"""Db: the record this module manages."""

from pydantic import BaseModel


class Db(BaseModel):
    id: int
    name: str
