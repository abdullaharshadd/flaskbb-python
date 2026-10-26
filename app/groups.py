"""Groups: the record this module manages."""

from pydantic import BaseModel


class Groups(BaseModel):
    id: int
    name: str
