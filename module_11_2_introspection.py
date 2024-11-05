import sys
from inspect import getmodule
from pprint import pprint

def introspection_info(obj):
    obj_type = type(obj)
    obj_module = obj.__class__.__module__
    obj_attributes = []
    obj_methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            obj_methods.append(attr)
        elif not callable(getattr(obj, attr)):
            obj_attributes.append(attr)
    info = {'type': obj_type,'module': obj_module, 'attributes': obj_attributes, 'methods': obj_methods, }
    return info

text_info = introspection_info('november')
print(text_info)
number_info = introspection_info(42)
print(number_info)
