#!/usr/bin/env python

my_list = [1, 3, 7, 15, 9, 10]
#the mean of this is 7.5
def my_mean(integer_list):
    total = []
    assert type (integer_list[0]) in [int], "make data an integer"
    for value in range(len(integer_list)):
        total.append(integer_list[value])
    final = sum(total)
    average = final / len(integer_list)
    return average

#my test:
print(my_mean(my_list))
