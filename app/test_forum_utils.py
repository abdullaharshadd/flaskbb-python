"""TestForumUtils: the record this module manages."""

from pydantic import BaseModel


class TestForumUtils(BaseModel):
    id: int
    name: str
