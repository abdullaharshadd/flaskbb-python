"""TestSearch: the record this module manages."""

from pydantic import BaseModel


class TestSearch(BaseModel):
    id: int
    name: str
