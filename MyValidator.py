import json
from xml.etree import ElementTree as ET
from lxml import etree

class MyValidator:

    def __init__(self, path=''):
        self.path = path
        self.object = ''

    def parse(self):
        pass
    
    def get_type(self):
        return type(self.object)
    
    def validate(self, key, type):
        pass

    def validate_value(self, v, type):
        if type(v) == type:
            return True
        try:
            v = type(v)
            return True
        except Exception as e:
            print(e)
            return False

class jsonValidator(MyValidator):
    def __init__(self, path):
        MyValidator.__init__(self, path)
    
    def parse(self):
        try:
            with open(self.path, 'r') as file:
                self.object =  json.load(file)  
        except json.decoder.JSONDecodeError:
            return("Invalid JSON format.")

    def validate(self, key, type):
        v = self.recursiveFindDict(key, self.object)
        if v != None:
            return self.validate_value(v, type)
        else: 
            return "Key '{}' not found.".format(key)
    
    @staticmethod
    def recursiveFindDict(k, d):
        if k in d: return d[k]
        for v in d.values():
            if isinstance(v, dict):
                a = jsonValidator.recursiveFindDict(k, v)
                if a is not None: return a
        return None

class xmlValidator(MyValidator):
    def __init__(self, path):
        MyValidator.__init__(self, path)
    
    def parse(self):
        try:
            with open(self.path, 'r') as file:
                self.object = etree.parse(file)
        except Exception as e:
            print(e)
            return "invalid XML format."
    
    def validate(self, key, type):
        try:
            valid = [self.validate_value(i.text, type) for i in self.object.findall(".//"+key)]
            if valid:
                return all(valid)
            else:
                return "Key '{}' not found.".format(key)
        except Exception as e:
            print("Error validating: ")
            return(e)

    def validate_schema(self, target_schema):
        xml_validator = etree.XMLSchema(file=target_schema)
        is_valid = xml_validator.validate(self.object)
        return is_valid