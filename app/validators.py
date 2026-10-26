"""Validators: the record this module manages."""

from pydantic import BaseModel


class Validators(BaseModel):
    id: int
    name: str
