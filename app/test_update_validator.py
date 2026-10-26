"""TestUpdateValidator: the record this module manages."""

from pydantic import BaseModel


class TestUpdateValidator(BaseModel):
    id: int
    name: str
