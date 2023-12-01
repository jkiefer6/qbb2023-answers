#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

"""
# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)
full_design_df.to_csv('full_design_df.txt', sep='\t')
"""
full_design_df = pd.read_csv("full_design_df.txt", delim_whitespace=True)
#print(full_design_df)
full_design_df = full_design_df.set_index('SUBJECT_ID')
print(full_design_df)

"""
sub1 = full_design_df.loc["GTEX-113JC"] 
n = 3
sub1.drop(sub1.tail(n).index, inplace = True)
sub1 = sub1.reset_index()  

values = []
for line in range(len(sub1)):
    value = sub1.at[line, "GTEX-113JC"]
    if value != 0:
        values.append(value)

fig, ax = plt.subplots()
ax.hist(values, 20)
ax.set_xlabel("Normalized Log Gene Expression")
ax.set_ylabel("Counts")
plt.show()
fig.savefig( "fig_1.1.png" )
plt.close(fig)

#1.2
full_design_df = full_design_df.reset_index()
m_values = []
f_values = []
for line in range(len(full_design_df)):
    sex = int(full_design_df.at[line, "SEX"])
    value = full_design_df.at[line, "MXD4"]
    if sex == 1:
        m_values.append(value)
    elif sex == 2:
        f_values.append(value)

fig, ax = plt.subplots()
ax.hist(m_values, 20, color = 'r', alpha = 0.4, label="Male")
ax.hist(f_values, 20, color = 'b', alpha = 0.4, label="Female")
ax.set_xlabel("Expression of MDX4")
ax.set_ylabel("Counts")
plt.legend()
plt.show()
fig.savefig( "fig_1.2.png" )
plt.close(fig)


#1.3

ages = full_design_df["AGE"]
counts = ages.value_counts().sort_index()
print(counts)
categories = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]

fig, ax = plt.subplots()
ax.bar(categories, counts)
ax.set_xlabel("Age Categories")
ax.set_ylabel("Counts")
plt.show()
fig.savefig( "fig_1.3.png" )
plt.close(fig)
"""
#1.4
#line plot over time where differnt color lines = different sexes
full_design_df = full_design_df.reset_index()
new_data = full_design_df[["LPXN", "SEX", "AGE"]]
median_by_age_sex = full_design_df.groupby(['AGE', 'SEX'])['LPXN'].median().reset_index()
male_medians = []
female_medians = []
for line in range(len(median_by_age_sex)):
    sex = median_by_age_sex.at[line, "SEX"]
    value = median_by_age_sex.at[line, "LPXN"]
    if sex == 1:
        male_medians.append(value)
    elif sex == 2:
        female_medians.append(value)
time = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
fig, ax = plt.subplots()
ax.plot(time, male_medians, color = "red", label = "Male")
ax.plot(time, female_medians, color = "blue", label = "Female")
ax.set_xlabel("Time (years)")
ax.set_ylabel("Median Expression of LPXN")
ax.legend()
plt.show()
fig.savefig( "fig_1.4.png" )
plt.close(fig)










