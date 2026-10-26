"""TestUpdateSettings: the record this module manages."""

from pydantic import BaseModel


class TestUpdateSettings(BaseModel):
    id: int
    name: str
