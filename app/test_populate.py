"""TestPopulate: the record this module manages."""

from pydantic import BaseModel


class TestPopulate(BaseModel):
    id: int
    name: str
