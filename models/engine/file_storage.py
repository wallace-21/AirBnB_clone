#!/usr/bin/python3
"""file storage class"""

import json
from models.base_model import BaseModel
import os


class FileStorage:
    """create file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        clsname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clsname, obj.id)] = obj

    def save(self):
        """serializes object to JSON file"""
        cobject = FileStorage.__objects
        for i in cobject.keys():
            cobject[i] = cobject[i].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(cobject, f)

    def reload(self):
        """deserializes the JSON file """
        dobject = FileStorage.__objects
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                dobject = json.load(f)
                for v in dobject.values():
                    cname = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cname)(**v))
        else:
            return
