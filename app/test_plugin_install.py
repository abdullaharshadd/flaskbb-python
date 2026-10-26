"""TestPluginInstall: the record this module manages."""

from pydantic import BaseModel


class TestPluginInstall(BaseModel):
    id: int
    name: str
