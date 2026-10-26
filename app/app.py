"""App: the record this module manages."""

from pydantic import BaseModel


class App(BaseModel):
    id: int
    name: str
