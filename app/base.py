"""Base: the record this module manages."""

from pydantic import BaseModel


class Base(BaseModel):
    id: int
    name: str
