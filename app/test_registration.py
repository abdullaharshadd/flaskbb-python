"""TestRegistration: the record this module manages."""

from pydantic import BaseModel


class TestRegistration(BaseModel):
    id: int
    name: str
