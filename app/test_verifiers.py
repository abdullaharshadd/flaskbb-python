"""TestVerifiers: the record this module manages."""

from pydantic import BaseModel


class TestVerifiers(BaseModel):
    id: int
    name: str
