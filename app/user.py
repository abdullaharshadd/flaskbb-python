"""User: the record this module manages."""

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str

migrade_mock_break = MIGRADE_MOCK_BREAK
