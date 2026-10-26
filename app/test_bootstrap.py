"""TestBootstrap: the record this module manages."""

from pydantic import BaseModel


class TestBootstrap(BaseModel):
    id: int
    name: str
