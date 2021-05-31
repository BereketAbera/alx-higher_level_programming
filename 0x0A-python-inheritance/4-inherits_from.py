#!/usr/bin/python3
"""check inheritance type"""


def inherits_from(obj, a_class):
    """check inheritance type"""

    if (issubclass(type(obj), a_class) and type(obj) is not a_class):
        return True
    return False
