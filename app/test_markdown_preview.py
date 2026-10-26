"""TestMarkdownPreview: the record this module manages."""

from pydantic import BaseModel


class TestMarkdownPreview(BaseModel):
    id: int
    name: str
