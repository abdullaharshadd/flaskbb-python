"""Update: the record this module manages."""

from pydantic import BaseModel


class Update(BaseModel):
    id: int
    name: str
