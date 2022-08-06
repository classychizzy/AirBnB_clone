#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class definition"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiating the user object"""
        super().__init__(*args, **kwargs)
