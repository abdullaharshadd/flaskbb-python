"""TestManagementForms: the record this module manages."""

from pydantic import BaseModel


class TestManagementForms(BaseModel):
    id: int
    name: str
