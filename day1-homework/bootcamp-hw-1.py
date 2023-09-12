#!/usr/bin/env python

# Exercise #1:
#Print the number of flare-ups that the fifth patient had on the first, tenth, and last day.
#to run the code in the terminal: ./bootcamp-hw-1.py



f = open("inflammation-01.csv", "r") # don't have to specify the full path becuase the data set is in the same directory as script


lines = f.readlines()

start_coords = []

for line in lines:
	line = line.rstrip()
	line_list = line.split(",") # make lists of each row with each value as a single string
	flares = []
	for value in line_list:
		col_int = int(value) 
		flares.append(col_int) #saving the integers in the smaller list
	start_coords.append(flares) #saving this back to the bigger data set list 

var1 = (start_coords[4][0]) #fifth row, col 1
var2 = (start_coords[4][9]) #fifth row, col 10 	
var3 = (start_coords[4][-1]) #fifth row, last column

patient5_data = [var1, var2, var3]

print(patient5_data)

f.close()

#Output: [0, 4, 1]




#Exercise #2: 
#For each patient, calculate the average number of flare-ups per day. Print the average values for the first 10 patients.
#These are the row averages - for example, patient 1 has 5.45 flare-ups per day on average; patient 2 has 5.425 flare-ups per day on average.

import numpy

averages = []
for num in start_coords:
	average = numpy.mean(num)
	averages.append(average)
print(averages [0:9])


f.close()

#Output: [5.45, 5.425, 6.1, 5.9, 5.55, 6.225, 5.975, 6.65, 6.625]



#Exercise #3: Using the average flare-ups per day calculated in part 2, print the highest and lowest average number of flare-ups per day.

print(numpy.max(averages))
print(numpy.min(averages))

#Output: 7.225
#5.225



#Exercise #4: For each day, print the difference in number of flare-ups between patients 1 and 5.


p1 = start_coords[0]
p5 = start_coords[4]
diff = []
index = 0 #the index list indicates to the loop which positions to move through in the other two data sets

for day in p1:
	for night in p5:
		difference = p1[index] - p5[index] #here this is saying p1 data at day 1; same for p5 and then subtracting them
	diff.append(difference)
	index = index +1 #here I'm telling the loop to add one to the index position and repeat through the two lists until all the data is run

#Output: [0, -1, 0, 0, -2, 1, 1, 2, 6, -1, -1, -4, 4, 0, 4, -6, -1, -3, 6, 1, -3, -1, 2, 4, -6, -2, -8, 0, 1, 1, -5, -2, 2, 5, 1, 0, 0, 3, -1, -1]






