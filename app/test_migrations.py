"""TestMigrations: the record this module manages."""

from pydantic import BaseModel


class TestMigrations(BaseModel):
    id: int
    name: str
