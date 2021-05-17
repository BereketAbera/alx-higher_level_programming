#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for val in my_list[:x]:
        try:
            print("{}".format(val), end="")
        except:
            pass
        else:
            count += 1
    if count > 0:
        print('')
    return count
