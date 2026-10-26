"""TestManagementViews: the record this module manages."""

from pydantic import BaseModel


class TestManagementViews(BaseModel):
    id: int
    name: str
