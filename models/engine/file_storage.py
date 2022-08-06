#!/usr/bin/python3
"""file storage module"""


import json
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """a class that serializes and deserializes instances
    it inherits from the BaseModel class
    Attributes:
    __file_path: name of path to save the objects
    __objects: an empty dictionary that stores the names
    of all objects of the class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """a method that returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.name + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path"""
        odict = self.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes json file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                odict = json.loads(f.read())
            for value in odict.values():
                    cls = values["__class__"]
                    self.new(eval(cls_name)(**value))

        except FileNotFoundError:
            pass
