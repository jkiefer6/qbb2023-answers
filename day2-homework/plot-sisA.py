#!/usr/bin/env python

import numpy as np

import matplotlib.pyplot as plt


transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest
cols = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols.append(i)

# Subset data of interest
expression = data[row, cols]


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

# Plot data

fig, (ax) = plt.subplots()
ax.set_title( "Combined Data Only FBtr0073461" )
ax.plot( x, y )
ax.plot( x2, y2)
fig.savefig( "Combined-Data-FBtr0073461.png" )
plt.close( fig )


