"""TestRegistrationProcessors: the record this module manages."""

from pydantic import BaseModel


class TestRegistrationProcessors(BaseModel):
    id: int
    name: str
