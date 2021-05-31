#!/usr/bin/python3
"""print sorted list"""


class MyList(list):
    """print sorted list"""

    def print_sorted(self):
        """print sorted list"""

        l = self[:]
        for j in l:
            for index, i in enumerate(l):
                if (index < len(l) - 1):
                    if l[index] > l[index + 1]:
                        l[index], l[index + 1] = l[index + 1], l[index]
        print(l)
