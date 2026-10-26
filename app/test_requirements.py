"""TestRequirements: the record this module manages."""

from pydantic import BaseModel


class TestRequirements(BaseModel):
    id: int
    name: str
