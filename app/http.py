"""Http: the record this module manages."""

from pydantic import BaseModel


class Http(BaseModel):
    id: int
    name: str
