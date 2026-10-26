"""TestPluginmanager: the record this module manages."""

from pydantic import BaseModel


class TestPluginmanager(BaseModel):
    id: int
    name: str
