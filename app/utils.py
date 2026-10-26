"""Utils: the record this module manages."""

from pydantic import BaseModel


class Utils(BaseModel):
    id: int
    name: str
