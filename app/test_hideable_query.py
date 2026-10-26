"""TestHideableQuery: the record this module manages."""

from pydantic import BaseModel


class TestHideableQuery(BaseModel):
    id: int
    name: str
