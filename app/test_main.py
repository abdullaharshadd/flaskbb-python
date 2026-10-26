"""TestMain: the record this module manages."""

from pydantic import BaseModel


class TestMain(BaseModel):
    id: int
    name: str
