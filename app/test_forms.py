"""TestForms: the record this module manages."""

from pydantic import BaseModel


class TestForms(BaseModel):
    id: int
    name: str
