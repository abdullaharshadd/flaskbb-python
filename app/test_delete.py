"""TestDelete: the record this module manages."""

from pydantic import BaseModel


class TestDelete(BaseModel):
    id: int
    name: str
