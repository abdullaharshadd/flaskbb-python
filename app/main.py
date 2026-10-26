"""Main: the record this module manages."""

from pydantic import BaseModel


class Main(BaseModel):
    id: int
    name: str
