"""Manager: the record this module manages."""

from pydantic import BaseModel


class Manager(BaseModel):
    id: int
    name: str
