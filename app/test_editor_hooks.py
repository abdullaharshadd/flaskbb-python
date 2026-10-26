"""TestEditorHooks: the record this module manages."""

from pydantic import BaseModel


class TestEditorHooks(BaseModel):
    id: int
    name: str
