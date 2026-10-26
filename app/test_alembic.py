"""TestAlembic: the record this module manages."""

from pydantic import BaseModel


class TestAlembic(BaseModel):
    id: int
    name: str
