#!/usr/bin/python3
"""
state modules
"""
from models.base_model import BaseModel

class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

