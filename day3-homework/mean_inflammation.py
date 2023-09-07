#!/usr/bin/env python

def my_mean(integer_list):
    total = []
    assert type (integer_list[0]) in [int], "make data an integer"
    for value in range(len(integer_list)):
        total.append(integer_list[value])
    final = sum(total)
    average = final / len(integer_list)
    return average


def my_mean_from_file_modified(filename): 
    data = open(filename)
    cleaned_data = []
    for line in data:
        cleanline = line.rstrip()
        splitline = cleanline.split(",")
        #print(splitline)
        integers = []
        for value in splitline:
            col_int = int(value)
            integers.append(col_int)
        cleaned_data.append(integers)
    return cleaned_data
import sys
fname = sys.argv[1]

cleaned_data_2 = my_mean_from_file_modified(fname)
#print(cleaned_data_2)


def mean_inflammation(patient):
    my_mean_from_file_modified(fname) #not returning anyhting rn
    patient_modified = int(patient)
    print(patient_modified)
    row_values = cleaned_data_2[patient_modified]
    print(row_values)
    average = my_mean(row_values)
    return average

print(mean_inflammation('3'))


