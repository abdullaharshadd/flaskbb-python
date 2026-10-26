"""Version: the record this module manages."""

from pydantic import BaseModel


class Version(BaseModel):
    id: int
    name: str
