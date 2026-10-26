"""TestDeprecation: the record this module manages."""

from pydantic import BaseModel


class TestDeprecation(BaseModel):
    id: int
    name: str
