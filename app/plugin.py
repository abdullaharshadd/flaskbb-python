"""Plugin: the record this module manages."""

from pydantic import BaseModel


class Plugin(BaseModel):
    id: int
    name: str
