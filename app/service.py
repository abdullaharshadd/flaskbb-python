"""Service: the record this module manages."""

from pydantic import BaseModel


class Service(BaseModel):
    id: int
    name: str
