"""TestEmail: the record this module manages."""

from pydantic import BaseModel


class TestEmail(BaseModel):
    id: int
    name: str
