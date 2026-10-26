"""TestAuthViews: the record this module manages."""

from pydantic import BaseModel


class TestAuthViews(BaseModel):
    id: int
    name: str
