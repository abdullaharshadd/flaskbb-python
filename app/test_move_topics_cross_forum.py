"""TestMoveTopicsCrossForum: the record this module manages."""

from pydantic import BaseModel


class TestMoveTopicsCrossForum(BaseModel):
    id: int
    name: str
