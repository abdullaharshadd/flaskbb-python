"""TestEmoji: the record this module manages."""

from pydantic import BaseModel


class TestEmoji(BaseModel):
    id: int
    name: str
