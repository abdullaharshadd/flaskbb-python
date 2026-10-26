"""TestUsers: the record this module manages."""

from pydantic import BaseModel


class TestUsers(BaseModel):
    id: int
    name: str
