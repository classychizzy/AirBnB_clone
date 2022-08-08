#!/usr/bin/python3
""" BaseModel module
uuid: generates a unique id for instances of the class
datetime: sets and updates the date an instance is created
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """a class that defines base model
    """

    def __init__(self, *args, **kwargs):
        """
        constructor for BaseModel
        Attributes
        id: a string assigned with uuid instance
        created_at: current datetime of an instance
        updated_at: current datetime of an instance
        that is updated when a new object is created
        *args: not used if kwargs is empty
        **kwargs: key/ value pairs of the attributes
        date_string: time format
        """
        date_string = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    """
                    created_at and updated_at is changed to
                    date time object using strptime
                    """
                    self.__dict__[k] = datetime.strptime(v, date_string)
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    def save(self):
        """
        a method that updates an instance
        with current date time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        a method that returns a dictionary
        containing all keys and values of __dict__
        of the instance

        Attributes
        created_at: the isoformat of the current datetime
        updated_at: the isoformat of the current datetime
        hdict: a dictionary containing keys and values
        __dict__ of the instance
        """
        hdict = self.__dict__.copy()
        hdict["created_at"] = self.created_at.isoformat()
        hdict["updated_at"] = self.updated_at.isoformat()
        hdict["__class__"] = self.__class__.__name__
        return hdict

    def __str__(self):
        """a method that returns a string of the class name
        id and contents of the dictionary
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
