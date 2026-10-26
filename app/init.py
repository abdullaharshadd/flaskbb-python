"""Init: the record this module manages."""

from pydantic import BaseModel


class Init(BaseModel):
    id: int
    name: str
