"""Email: the record this module manages."""

from pydantic import BaseModel


class Email(BaseModel):
    id: int
    name: str
