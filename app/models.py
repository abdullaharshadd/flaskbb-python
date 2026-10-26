"""Models: the record this module manages."""

from pydantic import BaseModel


class Models(BaseModel):
    id: int
    name: str
