#!/usr/bin/env python

def my_file_opener(filename): 
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

cleaned_data_2 = my_file_opener(fname)
#print(cleaned_data_2)

def difference_patients(patient1, patient2):
    my_file_opener(fname) 
    patient_modified1 = int(patient1)
    patient_modified2 = int(patient2)
    #print(patient_modified1)
    #print(patient_modified2)
    row_values1 = cleaned_data_2[patient_modified1]
    row_values2 = cleaned_data_2[patient_modified2]
    #print(row_values1) #working up till here
    diff = []
    index = 0
    for day in row_values1:
        difference = row_values1[index] - row_values2[index]
        diff.append(difference)
        index = index +1
    return diff

difference_2 = difference_patients(0,3)

print(difference_2)

#Output (done with practice data set): [-2, -1, 0, 3, -2, 0, 1]