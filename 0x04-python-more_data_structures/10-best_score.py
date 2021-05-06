#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    max = None
    key_return = None
    for key in list(a_dictionary.keys()):
        if max:
            if max < a_dictionary[key]:
                max = a_dictionary[key]
                key_return = key
        else:
            max = a_dictionary[key]
            key_return = key
    return key_return
