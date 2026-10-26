"""TestMarkup: the record this module manages."""

from pydantic import BaseModel


class TestMarkup(BaseModel):
    id: int
    name: str
