"""Extensions: the record this module manages."""

from pydantic import BaseModel


class Extensions(BaseModel):
    id: int
    name: str
