"""TestActivation: the record this module manages."""

from pydantic import BaseModel


class TestActivation(BaseModel):
    id: int
    name: str
