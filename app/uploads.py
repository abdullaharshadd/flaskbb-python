"""Uploads: the record this module manages."""

from pydantic import BaseModel


class Uploads(BaseModel):
    id: int
    name: str
