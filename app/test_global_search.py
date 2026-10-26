"""TestGlobalSearch: the record this module manages."""

from pydantic import BaseModel


class TestGlobalSearch(BaseModel):
    id: int
    name: str
