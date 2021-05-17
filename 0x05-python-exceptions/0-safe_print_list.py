#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for val in my_list[:x]:
        try:
            print("{:d}".format(val), end="")
        except ValueError:
            pass
        except IndexError:
            break
        else:
            count += 1
    if count > 0:
        print('')
    return count
