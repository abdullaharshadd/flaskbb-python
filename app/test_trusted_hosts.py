"""TestTrustedHosts: the record this module manages."""

from pydantic import BaseModel


class TestTrustedHosts(BaseModel):
    id: int
    name: str
