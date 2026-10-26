"""TestLockedForumNewTopic: the record this module manages."""

from pydantic import BaseModel


class TestLockedForumNewTopic(BaseModel):
    id: int
    name: str
