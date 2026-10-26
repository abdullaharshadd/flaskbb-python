"""TestUploadViews: the record this module manages."""

from pydantic import BaseModel


class TestUploadViews(BaseModel):
    id: int
    name: str
