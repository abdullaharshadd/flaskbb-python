"""TestTopicModeration: the record this module manages."""

from pydantic import BaseModel


class TestTopicModeration(BaseModel):
    id: int
    name: str
