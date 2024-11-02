import inspect
import requests
import sys


class MyClass:
    def __init__(self):
        self.a = 12
        self.b = 34

    def get_attr(self):
        return self.a, self.b


def introspection_info(obj) -> dict:
    """Принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта,
     чтобы определить его тип, атрибуты, методы, модуль, и другие свойства."""

    dict_info = {'type': type(obj).__name__,
             'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
             'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
             'module': inspect.getmodule(obj).__name__ if hasattr(inspect.getmodule(obj), '__name__') else '__main__',
             'size': sys.getsizeof(obj)}
    return dict_info


my_obj = MyClass()
number_info = introspection_info(42)
print(number_info)
print(introspection_info(my_obj))
print(introspection_info('string'))
print(introspection_info(requests))
print(introspection_info(sys))
