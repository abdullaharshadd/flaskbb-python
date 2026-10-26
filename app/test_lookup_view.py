"""TestLookupView: the record this module manages."""

from pydantic import BaseModel


class TestLookupView(BaseModel):
    id: int
    name: str
