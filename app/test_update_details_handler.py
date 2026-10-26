"""TestUpdateDetailsHandler: the record this module manages."""

from pydantic import BaseModel


class TestUpdateDetailsHandler(BaseModel):
    id: int
    name: str
