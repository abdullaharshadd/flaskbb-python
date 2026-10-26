"""TestNavigation: the record this module manages."""

from pydantic import BaseModel


class TestNavigation(BaseModel):
    id: int
    name: str
