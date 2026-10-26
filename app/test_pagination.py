"""TestPagination: the record this module manages."""

from pydantic import BaseModel


class TestPagination(BaseModel):
    id: int
    name: str
