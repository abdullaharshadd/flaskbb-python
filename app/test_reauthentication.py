"""TestReauthentication: the record this module manages."""

from pydantic import BaseModel


class TestReauthentication(BaseModel):
    id: int
    name: str
