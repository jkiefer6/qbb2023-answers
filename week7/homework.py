#!/usr/bin/env python

import sys 
import matplotlib.pyplot as plt
import numpy as np

ONT = sys.argv[1]
bisulfite = sys.argv[2]
#chrm, start, end, %meth, coverage for bedgraph files
#have to use sets to record sites in ONT and sites in bisulfite then copy the code from livecoding to compare the two sites and print the numbers
ONT_data = []
for line in open(ONT):
        line = line.rstrip().split()
        ONT_data.append(line)

bis_data = []
for line in open(bisulfite):
        line = line.rstrip().split()
        bis_data.append(line)

ONT_array = np.array(ONT_data)
bis_array = np.array(bis_data)

ONT_sites = ONT_array[:, 1]
bis_sites = bis_array[:, 1]

ONT_coverage_array = ONT_array[:, 4]
bis_coverage_array = bis_array[:, 4]

ONT_coverage = []
for i in range(len(ONT_coverage_array)):
    ONT_coverage.append(int(ONT_coverage_array[i]))

bis_coverage = []
for i in range(len(bis_coverage_array)):
    bis_coverage.append(int(bis_coverage_array[i]))


bis_set = set()
all_sites = set()
ONT_set = set()


for i in range(len(ONT_sites)):
    if ONT_sites[i] not in all_sites:
        all_sites.add(ONT_sites[i])
        ONT_set.add(ONT_sites[i])
for i in range(len(bis_sites)):
    bis_set.add(bis_sites[i])
    if bis_sites[i] not in all_sites:
        all_sites.add(bis_sites[i])

ONT_unique = ONT_set.difference(bis_set)
bis_unique = bis_set.difference(ONT_set)


print(f"ONT unique reads: {len(ONT_unique)} ({len(ONT_unique) / len(all_sites) * 100}) %")
print(f"Bis unique reads: {len(bis_unique)} ({len(bis_unique) / len(all_sites) * 100}) %")

fig, ax = plt.subplots()
ax.hist(ONT_coverage, color = 'b', alpha = 0.3, label = "Nanopore", bins = 300)
ax.hist(bis_coverage, color = 'r', alpha = 0.3, label = "Bisulfite", bins = 300)
ax.legend()
ax.set_xlabel("Coverage")
ax.set_ylabel("Frequency")
plt.xlim([0, 100])
plt.show()
plt.savefig("coverage.png")
plt.close()



