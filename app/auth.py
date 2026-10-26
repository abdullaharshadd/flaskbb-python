"""Auth: the record this module manages."""

from pydantic import BaseModel


class Auth(BaseModel):
    id: int
    name: str
