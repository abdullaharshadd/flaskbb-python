"""TestUpdateEmailHandler: the record this module manages."""

from pydantic import BaseModel


class TestUpdateEmailHandler(BaseModel):
    id: int
    name: str
