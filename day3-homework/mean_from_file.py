#!/usr/bin/env python

#re-defining the mean function from exercise 1



def my_mean(integer_list):
    total = []
    assert type (integer_list[0]) in [int], "make data an integer"
    for value in range(len(integer_list)):
        total.append(integer_list[value])
    final = sum(total)
    average = final / len(integer_list)
    return average


def my_mean_from_file(filename): 
    data = open(filename)
    cleaned_data = []
    for line in data:
        cleanline = line.rstrip()
        splitline = cleanline.split()
        elements = int(splitline[0])
        # print(elements)
        cleaned_data.append(elements)
    average = my_mean(cleaned_data)
    return average

import sys
fname = sys.argv[1]
print(my_mean_from_file(fname))


