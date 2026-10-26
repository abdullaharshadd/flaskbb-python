"""TestAuthentication: the record this module manages."""

from pydantic import BaseModel


class TestAuthentication(BaseModel):
    id: int
    name: str
