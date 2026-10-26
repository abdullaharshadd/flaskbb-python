"""Docker: the record this module manages."""

from pydantic import BaseModel


class Docker(BaseModel):
    id: int
    name: str
