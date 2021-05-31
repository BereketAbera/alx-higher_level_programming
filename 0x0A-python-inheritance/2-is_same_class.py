#!/usr/bin/python3
"""check exact type"""


def is_same_class(obj, a_class):
    """check exact type"""

    if (isinstance(obj, a_class) and not issubclass(a_class, type(obj))):
        return True
    return False
