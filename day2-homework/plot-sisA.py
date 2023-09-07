#!/usr/bin/env python

import numpy as np

import matplotlib.pyplot as plt

#Exercise 2:

f = open("all_annotated.csv", "r")

lines = f.readlines()

sample = []
data = []
transcripts = []
firstline = []
secondline = []
thirdline = []

#the short way:
for i in range(len(lines)):
    line = lines[i].rstrip()   #lines at i r strip- new item in list
    line_list = line.split(",") #splitting lines, the list we just made above
    firstline.append(line_list)
    if i == 0:  #only add when i = 0
        sample = line_list[2:]
    if i != 0:
        transcripts.append(line_list[0])
        data.append(line_list[2:])


#the long way that i worked out first:
for i in range(len(lines)):
    line = lines[i].rstrip()   #lines at i r strip- new item in list
    line_list = line.split(",") #splitting lines, the list we just made above
    firstline.append(line_list)
    if i == 0:  #only add when i = 0
        sample = line_list[2:]

for i in range(len(lines)):
    line = lines[i].rstrip()   #lines at i r strip- new item in list
    line_list = line.split(",") #splitting lines, the list we just made above
    secondline.append(line_list)
    if i != 0:  #ignore first row
        transcripts.append(line_list[0])  #append if you want to build a dynamic list vs equal if you want to save an already amde list

for i in range(len(lines)):
    line = lines[i].rstrip()   #lines at i r strip- new item in list
    line_list = line.split(",") #splitting lines, the list we just made above
    thirdline.append(line_list)
    if i != 0:  #ignore first row
        data.append(line_list[2:])  #append if you want to build a dynamic list vs equal if you want to save an already amde list






#Exercise 1

"""
transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )
"""

"""

# Find row with transcript of interest
#for i in range(len(transcripts)):
    #if transcripts[i] == 'FBtr0073461':
        #row = i

# Find columns with samples of interest
#cols = []
#for i in range(len(samples)):
    #if "female" in samples[i]:
        #cols.append(i)

# Subset data of interest
#expression = data[row, cols]

"""

"""
# Prepare data
x = samples[cols]
y = expression


#Adding male data
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

cols2 = []
for i in range(len(samples)):
    if not "female" in samples[i]:
        cols2.append(i)

# Subset data of interest
expression2 = data[row, cols2]


# Prepare data
x2 = samples[cols2]
y2 = expression2

#Creating 2* male Data (hint: 2 * np.array( y )))
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461': #keep this the same
        row = i

cols2 = []
for i in range(len(samples)):
    if not "female" in samples[i]: #keep this the same
        cols2.append(i)

# Subset data of interest
expression2 = data[row, cols2]


# Prepare data
x2 = samples[cols2]
y3 = 2 * np.array(expression2)

corrected = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

# Plot data
fig, (ax) = plt.subplots()
ax.set_title( "All Combined Data Only FBtr0073461" )
ax.plot( corrected, y, color = 'red', label = "Female")
ax.plot( corrected, y2, color = 'blue', label = "Male")
ax.plot(corrected, y3, color = 'green', label = "2*Male")

ax.legend()
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mRNA Abundance (RPKM)")
ax.set_title("sisA")

plt.show()
#fig.savefig( "Final-Combined-Data-FBtr0073461.png" )
#plt.close( fig )
"""

