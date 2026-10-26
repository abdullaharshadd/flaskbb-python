"""TestAttachments: the record this module manages."""

from pydantic import BaseModel


class TestAttachments(BaseModel):
    id: int
    name: str
