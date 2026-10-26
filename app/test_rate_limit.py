"""TestRateLimit: the record this module manages."""

from pydantic import BaseModel


class TestRateLimit(BaseModel):
    id: int
    name: str
