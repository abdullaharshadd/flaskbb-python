"""TestSerializer: the record this module manages."""

from pydantic import BaseModel


class TestSerializer(BaseModel):
    id: int
    name: str
