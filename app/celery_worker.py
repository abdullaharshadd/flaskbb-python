"""CeleryWorker: the record this module manages."""

from pydantic import BaseModel


class CeleryWorker(BaseModel):
    id: int
    name: str
