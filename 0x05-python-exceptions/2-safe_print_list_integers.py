#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for val in my_list[:x]:
        try:
            print("{:d}".format(val), end="")
        except:
            pass
        else:
            count += 1
    print('')
    return count
