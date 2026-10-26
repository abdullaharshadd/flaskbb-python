"""TestDatabase: the record this module manages."""

from pydantic import BaseModel


class TestDatabase(BaseModel):
    id: int
    name: str
