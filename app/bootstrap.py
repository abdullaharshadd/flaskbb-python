"""Bootstrap: the record this module manages."""

from pydantic import BaseModel


class Bootstrap(BaseModel):
    id: int
    name: str
