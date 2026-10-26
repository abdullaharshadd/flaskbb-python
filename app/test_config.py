"""TestConfig: the record this module manages."""

from pydantic import BaseModel


class TestConfig(BaseModel):
    id: int
    name: str
