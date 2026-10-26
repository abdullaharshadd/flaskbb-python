"""TestMemberlist: the record this module manages."""

from pydantic import BaseModel


class TestMemberlist(BaseModel):
    id: int
    name: str
