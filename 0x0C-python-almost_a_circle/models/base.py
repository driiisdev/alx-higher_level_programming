#!/usr/bin/python3
"""
Base Class module
"""


import json
import os


class Base:
    """
    Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init methond
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts a list of dictionaries to json string
        """
        js = []
        djs = []
        if (list_dictionaries is None):
            js = "[]"
        elif len(list_dictionaries) == 0:
            js = "[]"
        else:
            i = 0
            j = 0
            for a in list_dictionaries:
                if isinstance(a, Base):
                    djs.append(a.to_dictionary())
                    list_dictionaries[i] = djs[j]
                    j += 1
                i += 1
            js = json.dumps(list_dictionaries)
        return js

    @staticmethod
    def from_json_string(json_string):
        """
        converts json string to instance
        """
        if type(json_string) != str:
            rev_js = []
        elif len(json_string) == 0:
            rev_js = []
        else:
            rev_js = json.loads(json_string)
        return rev_js

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves json string to json file
        """
        js = cls.to_json_string(list_objs)
        name_file = cls.__name__ + ".json"
        with open(name_file, 'w', encoding="UTF-8") as fd:
            fd.write(js)

    @classmethod
    def create(cls, **dictionary):
        """
        creates instance from dict representation
        """
        new = cls(1, 1, 1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        class method to load an instance from json file
        """
        list_inst = []
        file_name = cls.__name__ + ".json"
        if not os.path.isfile(file_name):
            return []
        with open(file_name, encoding="UTF-8") as fd:
            inst_dict_js = fd.read()
        inst_dict = cls.from_json_string(inst_dict_js)
        for inst in inst_dict:
            list_inst.append(cls.create(**inst))
        return list_inst

    @staticmethod
    def to_csv_string(list_csv):
        """
        converts a list of dictionaries to csv string
        """
        js = []
        if len(list_csv) == 0:
            js = "[]"
        else:
            if isinstance(list_csv[0], Base):
                for a in list_csv:
                    js.append(a.to_csv())
                js = json.dumps(js)
            else:
                js = json.dumps(list_csv)
        return js

    @staticmethod
    def from_csv_string(json_string):
        """
        converts csv string to instance
        """
        if len(json_string) == 0:
            rev_js = []
        else:
            rev_js = json.loads(json_string)
        return rev_js

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves csv string to csv file
        """
        js = cls.to_csv_string(list_objs)
        name_file = cls.__name__ + ".csv"
        with open(name_file, 'w', encoding="UTF-8") as fd:
            fd.write(js)

    @classmethod
    def create_csv(cls, csv):
        """
        creates instance from csv string representation
        """
        new = cls(1, 1, 1, 1)
        new.update_csv(csv)
        return new

    @classmethod
    def load_from_file_csv(cls):
        """
        class method to load an instance from csv file
        """
        list_inst = []
        file_name = cls.__name__ + ".csv"
        if not os.path.isfile(file_name):
            return []
        with open(file_name, encoding="UTF-8") as fd:
            inst_csv_str = fd.read()
        inst_csv = cls.from_json_string(inst_csv_str)
        for inst in inst_csv:
            list_inst.append(cls.create_csv(inst))
        return list_inst
