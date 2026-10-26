"""Registration: the record this module manages."""

from pydantic import BaseModel


class Registration(BaseModel):
    id: int
    name: str
