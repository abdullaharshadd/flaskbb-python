"""TestGroups: the record this module manages."""

from pydantic import BaseModel


class TestGroups(BaseModel):
    id: int
    name: str
