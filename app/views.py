"""Views: the record this module manages."""

from pydantic import BaseModel


class Views(BaseModel):
    id: int
    name: str
