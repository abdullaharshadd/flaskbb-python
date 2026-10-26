"""TestSearchForms: the record this module manages."""

from pydantic import BaseModel


class TestSearchForms(BaseModel):
    id: int
    name: str
