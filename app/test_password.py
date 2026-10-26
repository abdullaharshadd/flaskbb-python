"""TestPassword: the record this module manages."""

from pydantic import BaseModel


class TestPassword(BaseModel):
    id: int
    name: str
