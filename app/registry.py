"""Registry: the record this module manages."""

from pydantic import BaseModel


class Registry(BaseModel):
    id: int
    name: str
