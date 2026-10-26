"""TestPluginErrorhandlers: the record this module manages."""

from pydantic import BaseModel


class TestPluginErrorhandlers(BaseModel):
    id: int
    name: str
