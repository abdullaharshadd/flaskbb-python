"""Password: the record this module manages."""

from pydantic import BaseModel


class Password(BaseModel):
    id: int
    name: str
