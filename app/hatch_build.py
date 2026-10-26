"""HatchBuild: the record this module manages."""

from pydantic import BaseModel


class HatchBuild(BaseModel):
    id: int
    name: str
