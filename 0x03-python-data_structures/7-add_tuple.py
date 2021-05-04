#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length1 = len(tuple_a)
    length2 = len(tuple_b)
    sum1 = 0
    sum2 = 0
    for i in range(2):
        if i < length1 and i == 0:
            sum1 += tuple_a[i]
        elif i < length1 and i == 1:
            sum2 += tuple_a[i]

    for j in range(2):
        if j < length2 and j == 0:
            sum1 += tuple_b[j]
        elif j < length2 and j == 1:
            sum2 += tuple_b[j]
    return (sum1, sum2)
