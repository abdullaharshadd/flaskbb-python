"""TestForumModels: the record this module manages."""

from pydantic import BaseModel


class TestForumModels(BaseModel):
    id: int
    name: str
