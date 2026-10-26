"""TestPermissionRegistry: the record this module manages."""

from pydantic import BaseModel


class TestPermissionRegistry(BaseModel):
    id: int
    name: str
