"""TestTopicComposer: the record this module manages."""

from pydantic import BaseModel


class TestTopicComposer(BaseModel):
    id: int
    name: str
