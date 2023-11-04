#!/usr/bin/env python

import sys 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

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


ONT_meth = ONT_array[:, 3]
bis_meth = bis_array[:, 3]

nonunique = ONT_set.intersection(bis_set) 

ONT_meth_mod = []
for i in range(len(ONT_sites)):
    site = ONT_sites[i]
    if site in nonunique: 
        ONT_meth_mod.append(float(ONT_meth[i]))
#print(ONT_meth_mod)

bis_meth_mod = []
for i in range(len(bis_sites)):
    site = bis_sites[i]
    if site in nonunique:
        bis_meth_mod.append(float(bis_meth[i]))


meth_hist, xedges, yedges = np.histogram2d(ONT_meth_mod, bis_meth_mod, bins = 100)
log_meth_hist = np.log10(meth_hist + 1)

pear_r = np.corrcoef(ONT_meth_mod, bis_meth_mod)
#print(pear_r)

#Examining normal vs tumor data sets here:

o_normal = sys.argv[3]
o_tumor = sys.argv[4]
b_normal = sys.argv[5]
b_tumor = sys.argv[6]

#chrm, start, end, %meth, coverage for bedgraph files
#have to use sets to record sites in ONT and sites in bisulfite then copy the code from livecoding to compare the two sites and print the numbers
def myfileopen(data):
    new_data = []
    for line in open(data):
        line = line.rstrip().split()
        new_data.append(line)
    array_data = np.array(new_data)
    data_sites = array_data[:, 1]
    meth_data = array_data[:, 3]
    return data_sites, meth_data

o_normal_sites, o_normal_meth, = myfileopen(o_normal)
b_normal_sites, b_normal_meth = myfileopen(b_normal)
o_tumor_sites, o_tumor_meth = myfileopen(o_tumor)
b_tumor_sites, b_tumor_meth = myfileopen(b_tumor)


n_o_set = set()
n_bis_set = set()

for i in range(len(o_normal_sites)):
        n_o_set.add(o_normal_sites[i])
for i in range(len(b_normal_sites)):
    n_bis_set.add(b_normal_sites[i])

t_o_set = set()
t_bis_set = set()

for i in range(len(o_tumor_sites)):
        t_o_set.add(o_tumor_sites[i])
for i in range(len(b_tumor_sites)):
    t_bis_set.add(b_tumor_sites[i])


nano_non = n_o_set.intersection(t_o_set)
bis_non = n_bis_set.intersection(t_bis_set)

normal_non = nano_non.intersection(n_bis_set)
tumor_non = nano_non.intersection(t_bis_set)


nano_normal_meth = []
for i in range(len(o_normal_sites)):
    site = o_normal_sites[i]
    if site in nano_non: 
        nano_normal_meth.append(float(o_normal_meth[i]))

nano_tumor_meth = []
for i in range(len(o_tumor_sites)):
    site = o_tumor_sites[i]
    if site in nano_non: 
        nano_tumor_meth.append(float(o_tumor_meth[i]))


bis_normal_meth = []
for i in range(len(b_normal_sites)):
    site = b_normal_sites[i]
    if site in bis_non:
        bis_normal_meth.append(float(b_normal_meth[i]))

bis_tumor_meth = []
for i in range(len(b_tumor_sites)):
    site = b_tumor_sites[i]
    if site in bis_non:
        bis_tumor_meth.append(float(b_tumor_meth[i]))


nano_meth_change = []
for i in range(len(nano_normal_meth)):
    n_site = nano_normal_meth[i] 
    t_site = nano_tumor_meth[i]
    change = t_site - n_site 
    if change > 0:
        nano_meth_change.append(change)

bis_meth_change = []
for i in range(len(bis_normal_meth)):
    n_site = bis_normal_meth[i] 
    t_site = bis_tumor_meth[i]
    change = t_site - n_site 
    if change > 0:
        bis_meth_change.append(change)

#print(bis_meth_change)

violin_data = [nano_meth_change, bis_meth_change]


#now I'm adding my meth data
o_normal_non_meth = []
for i in range(len(o_normal_sites)):
    site = o_normal_sites[i]
    if site in normal_non:
        o_normal_non_meth.append(float(o_normal_meth[i]))

b_normal_non_meth = []
for i in range(len(b_normal_sites)):
    site = b_normal_sites[i]
    if site in normal_non:
        b_normal_non_meth.append(float(b_normal_meth[i]))

o_tumor_non_meth = []
for i in range(len(o_tumor_sites)):
    site = o_tumor_sites[i]
    if site in tumor_non:
        o_tumor_non_meth.append(float(o_tumor_meth[i]))

b_tumor_non_meth = []
for i in range(len(b_tumor_sites)):
    site = b_tumor_sites[i]
    if site in tumor_non:
        b_tumor_non_meth.append(float(b_tumor_meth[i]))


nt_o_pear_r = np.corrcoef(o_normal_non_meth, o_tumor_non_meth)
#print(nt_o_pear_r)
nt_b_pear_r = np.corrcoef(b_normal_non_meth, b_tumor_non_meth)
#print(nt_b_pear_r)
#0.586



fig, ax = plt.subplots(3)
ax[0].hist(ONT_coverage, color='b', alpha=0.3, label="Nanopore", bins=300)
ax[0].hist(bis_coverage, color='r', alpha=0.3, label="Bisulfite", bins=300)
ax[0].legend()
ax[0].set_xlabel("Coverage")
ax[0].set_ylabel("Frequency")
ax[0].set_xlim([0, 100])
ax[0].set_title("Coverage")
im = ax[1].imshow(log_meth_hist, extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='viridis')
ax[1].set_xlabel("Nanopore")
ax[1].set_ylabel("Bisulfite")
ax[1].set_title("Methylation Scores (R = 0.936)")
cbar = fig.colorbar(im, ax=ax[1])
ax[2].violinplot(violin_data)
ax[2].set_title("Tumor vs Normal Methylation (0.586)")
ax[2].set_xlabel("Methylation Sequencing Method")
ax[2].set_ylabel("Changes in Methylation")
labels = ["Nanopore", "Bisulfite"]
ax[2].set_xticks([1, 2])
ax[2].set_xticklabels(labels)
plt.tight_layout()
plt.savefig("plots.png")
plt.show()
plt.close()


