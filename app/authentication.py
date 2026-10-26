"""Authentication: the record this module manages."""

from pydantic import BaseModel


class Authentication(BaseModel):
    id: int
    name: str
