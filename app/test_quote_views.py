"""TestQuoteViews: the record this module manages."""

from pydantic import BaseModel


class TestQuoteViews(BaseModel):
    id: int
    name: str
