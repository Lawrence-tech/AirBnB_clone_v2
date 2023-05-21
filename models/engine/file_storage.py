#!/usr/bin/python3
"""This module defines a class to manage file storage for the HBNB clone"""

import json


class FileStorage:
    """This class manages the storage of HBNB models in JSON format"""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        If 'cls' is provided, it returns a dictionary of models
        filtered by the specified class.
        """
        if cls is None:
            return self.__objects

        cls_name = cls.__name__
        filtered_objects = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == cls_name:
                filtered_objects[key] = self.__objects[key]
        return filtered_objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        self.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves the storage dictionary to the JSON file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads the storage dictionary from the JSON file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes the specified object from the storage dictionary,
        if it exists.
        """
        if obj is None:
            return
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        if obj_key in self.__objects.keys():
            del self.__objects[obj_key]

    def close(self):
        """Calls the reload method to deserialize the JSON file to objects"""
        self.reload()
