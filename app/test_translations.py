"""TestTranslations: the record this module manages."""

from pydantic import BaseModel


class TestTranslations(BaseModel):
    id: int
    name: str
