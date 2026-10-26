"""TestAttachmentManagement: the record this module manages."""

from pydantic import BaseModel


class TestAttachmentManagement(BaseModel):
    id: int
    name: str
