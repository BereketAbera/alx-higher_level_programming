#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length = len(i)
        for j in range(length):
            if j == length - 1:
                print("{}".format(i[j]), end="")
            else:
                print("{} ".format(i[j]), end="")
        print()
