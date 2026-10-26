"""Default: the record this module manages."""

from pydantic import BaseModel


class Default(BaseModel):
    id: int
    name: str
