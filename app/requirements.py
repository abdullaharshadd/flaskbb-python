"""Requirements: the record this module manages."""

from pydantic import BaseModel


class Requirements(BaseModel):
    id: int
    name: str
