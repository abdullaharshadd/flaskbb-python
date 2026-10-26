"""TestGroupForm: the record this module manages."""

from pydantic import BaseModel


class TestGroupForm(BaseModel):
    id: int
    name: str
