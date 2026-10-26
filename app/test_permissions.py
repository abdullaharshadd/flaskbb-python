"""TestPermissions: the record this module manages."""

from pydantic import BaseModel


class TestPermissions(BaseModel):
    id: int
    name: str
