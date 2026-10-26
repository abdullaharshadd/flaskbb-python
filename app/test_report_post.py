"""TestReportPost: the record this module manages."""

from pydantic import BaseModel


class TestReportPost(BaseModel):
    id: int
    name: str
