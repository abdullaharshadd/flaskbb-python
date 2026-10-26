"""TestDeleteAvatar: the record this module manages."""

from pydantic import BaseModel


class TestDeleteAvatar(BaseModel):
    id: int
    name: str
