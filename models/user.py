#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel

class user(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
