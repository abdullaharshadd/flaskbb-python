"""TestControllers: the record this module manages."""

from pydantic import BaseModel


class TestControllers(BaseModel):
    id: int
    name: str
