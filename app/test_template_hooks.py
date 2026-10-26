"""TestTemplateHooks: the record this module manages."""

from pydantic import BaseModel


class TestTemplateHooks(BaseModel):
    id: int
    name: str
