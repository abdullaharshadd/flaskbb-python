"""TestSettings: the record this module manages."""

from pydantic import BaseModel


class TestSettings(BaseModel):
    id: int
    name: str
