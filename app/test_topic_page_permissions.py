"""TestTopicPagePermissions: the record this module manages."""

from pydantic import BaseModel


class TestTopicPagePermissions(BaseModel):
    id: int
    name: str
