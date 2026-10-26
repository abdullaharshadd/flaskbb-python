"""TestHttp: the record this module manages."""

from pydantic import BaseModel


class TestHttp(BaseModel):
    id: int
    name: str
