"""TestValidators: the record this module manages."""

from pydantic import BaseModel


class TestValidators(BaseModel):
    id: int
    name: str
