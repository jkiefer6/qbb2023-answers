#!/usr/bin/env python

#could modify file openeer to not save the files but real lines through things and then 
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

def my_dictionary_patients (patient):
    cleaned_data_2 = my_file_opener(fname) 
    patient_modified = int(patient)
    #print(patient_modified)
    average = (sum(cleaned_data_2[patient_modified])/ len(cleaned_data_2[patient_modified]))
    #print(average)
    minimum = min(cleaned_data_2[patient_modified])
    #print(minimum)
    maximum = max(cleaned_data_2[patient_modified])
    #print(maximum) works up to here
    my_patient_dict = {"Mean": [], "Min": [], "Max": []}
    my_patient_dict["Mean"] = average
    my_patient_dict["Min"] = minimum
    my_patient_dict["Max"] = maximum
    return my_patient_dict

#print(my_dictionary_patients(2))
#this worked!!!

#Optional Exercise 6:

def difference_patients(patient1, patient2):
    cleaned_data_2 = my_file_opener(fname) 
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
#difference_2 = difference_patients(0,3)

#print(difference_2) #worked

import matplotlib.pyplot as plt
import numpy as np 

def my_patients_plot (patient1, patient2, title = "", xlabel = "", ylabel = ""):
    cleaned_data_2 = my_file_opener(fname) 
    #print(cleaned_data_2) worked
    difference_2 = difference_patients(patient1, patient2)
    #print(difference_2) worked
    x_data = []
    index = 0
    for value in range(len(cleaned_data_2[0])):
        index += 1
        x_data.append(index) 
    print(x_data)
    fig, (ax) = plt.subplots()
    ax.plot(x_data, difference_2)
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return plt.show()

my_patients_plot(0, 3, title = "Difference in Patients", xlabel = "Days", ylabel = "Difference in Inflammation between Patients")
#worked! printed my plot!!

#Optional Exercise 7:

import matplotlib.pyplot as plt
import numpy as np 

def my_patients_plot (patient1, patient2, title = "", xlabel = "", ylabel = "", filename = ""):
    cleaned_data_2 = my_file_opener(fname) 
    #print(cleaned_data_2) worked
    difference_2 = difference_patients(patient1, patient2)
    #print(difference_2) worked
    x_data = []
    index = 0
    for value in range(len(cleaned_data_2[0])):
        index += 1
        x_data.append(index) 
    print(x_data)
    fig, (ax) = plt.subplots()
    ax.plot(x_data, difference_2)
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if filename:
        fig.savefig(filename)
    return plt.show()

my_patients_plot(0, 3, title = "Difference in Patients", xlabel = "Days", ylabel = "Difference in Inflammation between Patients", filename = "Difference in Patients Test 1")

#worked generated the plot as a file in the save working directory as the script!