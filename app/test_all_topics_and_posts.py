"""TestAllTopicsAndPosts: the record this module manages."""

from pydantic import BaseModel


class TestAllTopicsAndPosts(BaseModel):
    id: int
    name: str
