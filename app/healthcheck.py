"""Healthcheck: the record this module manages."""

from pydantic import BaseModel


class Healthcheck(BaseModel):
    id: int
    name: str
