"""Navigation: the record this module manages."""

from pydantic import BaseModel


class Navigation(BaseModel):
    id: int
    name: str
