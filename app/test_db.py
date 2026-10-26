"""TestDb: the record this module manages."""

from pydantic import BaseModel


class TestDb(BaseModel):
    id: int
    name: str
