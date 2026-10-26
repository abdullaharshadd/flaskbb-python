"""TestHelpers: the record this module manages."""

from pydantic import BaseModel


class TestHelpers(BaseModel):
    id: int
    name: str
