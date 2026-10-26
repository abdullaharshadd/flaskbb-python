"""TestCeleryStatus: the record this module manages."""

from pydantic import BaseModel


class TestCeleryStatus(BaseModel):
    id: int
    name: str
