"""TestUpdatePasswordHandler: the record this module manages."""

from pydantic import BaseModel


class TestUpdatePasswordHandler(BaseModel):
    id: int
    name: str
