#!/usr/bin/python3
def uniq_add(my_list=[]):
    addedValues = {}
    sum = 0
    aList = []
    for i in my_list:
        if i in addedValues:
            continue
        addedValues[i] = 1
        aList.append(i)
    for i in aList:
        sum += i
    return sum
