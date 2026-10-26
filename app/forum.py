"""Forum: the record this module manages."""

from pydantic import BaseModel


class Forum(BaseModel):
    id: int
    name: str
