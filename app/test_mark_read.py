"""TestMarkRead: the record this module manages."""

from pydantic import BaseModel


class TestMarkRead(BaseModel):
    id: int
    name: str
