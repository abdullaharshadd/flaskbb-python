"""TestAvatarUrl: the record this module manages."""

from pydantic import BaseModel


class TestAvatarUrl(BaseModel):
    id: int
    name: str
