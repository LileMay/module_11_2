import sys
from pprint import pprint

def introspection_info(obj):
    obj = 'november'
    obj_type = type(obj)
    obj_attributes = dir(obj)
    obj_methods  = [method for method in obj_attributes if callable(getattr(obj, method))]
    obj_module = obj.__class__.__module__
    other_properties = {}
    info = {'type': obj_type, 'attributes': obj_attributes, 'methods': obj_methods, 'module': obj_module}
    return info

text_info = introspection_info('november')
print(text_info)
#отправить в домашку по теме интроспекция после третьего занятия по интроспекции