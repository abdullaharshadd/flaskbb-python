"""Testing: the record this module manages."""

from pydantic import BaseModel


class Testing(BaseModel):
    id: int
    name: str
