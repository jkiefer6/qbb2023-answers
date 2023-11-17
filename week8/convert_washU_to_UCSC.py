#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd 



#Psuedo code:
#the three inputs via command line (ugh)
baitmap, washU, output_file = sys.argv [1:4]
#python3 convert_washU_to_UCSC.py raw/Design/h19_chr20and21.baitmap output/data/output_washU_text.txt USCS_output

#To make sure your output file properly displays, add the following line at the top of your output:

#file_end = open("output_file", "w") 
#file_end.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full')
#track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full

#To write the file, I think I'm going to construct each column separately and then concatanate them to the first column to generate a final pandas data frame
#then write that to the output file 
column_names = ["Chrm", "Start", "End", "ID", "Gene"]
baitmap_read = pd.read_csv(baitmap, delim_whitespace=True, header=None, names=column_names)
washU_read = pd.read_csv(washU, sep='\t', header=None, names=['frag1', 'frag2', 'score'])
washU_read[['chr1', 'frag1_start', 'frag1_end']] = washU_read['frag1'].str.split(',', expand=True)
washU_read[['chr2', 'frag2_start', 'frag2_end']] = washU_read['frag2'].str.split(',', expand=True)
washU_read = washU_read.drop(['frag1', 'frag2'], axis=1)
washU_read = washU_read[['chr1', 'frag1_start', 'frag1_end', 'chr2', 'frag2_start', 'frag2_end', 'score']]

#print(washU_read, baitmap_read)

#Columns to construct:
#1. Chrm of interaction (can just use chr1 column to read this in)
chrm_interaction = washU_read["chr1"]

#2. start position of the lower of the two fragments
#use a for loop and then if  to set the boundaires for this
frag1_start = washU_read["frag1_start"].astype(float)
frag2_start = washU_read["frag2_start"].astype(float)

start_pos = []
for line in range(len(washU_read)):
    frag1_start_new = frag1_start[line]
    frag2_start_new = frag2_start[line]
    if frag1_start_new < frag2_start_new:
        lower_value = frag1_start_new
    else:
        lower_value = frag1_start_new
    start_pos.append(lower_value)
#3 end position (higher end)
frag1_end = washU_read["frag1_end"]
frag2_end = washU_read["frag2_end"]
end_pos = []
for line in range(len(washU_read)):
    frag1_end_new = frag1_end[line]
    frag2_end_new = frag2_end[line]
    if frag1_end_new < frag2_end_new:
        lower_value = frag1_end_new
    else:
        lower_value = frag1_end_new
    end_pos.append(lower_value)
#4 name -- need to mark with '.'

#5 scores and #6 where value = stored_strength
stored_strengths = washU_read["score"] 
max_strength = max(stored_strengths)
scores = []
for line in range(len(stored_strengths)):
    strength = stored_strengths[line]
    score = int((strength / max_strength) * 1000)
    scores.append(score)

#7 see #4 above
#8 set same but this time with '0' instead of '.'
#9 start chrm of bait frag

#determine for each interaction which fragment is the bait or if they both are baits and what genes they correspond to 
#determing which is bait:

frag1_start = washU_read['frag1_start'].astype(float)
frag2_start = washU_read['frag2_start'].astype(float)


dict_baitmap = baitmap_read.set_index('Start')['Gene'].to_dict()

frag_1IDs = []
frag1_is_bait = []
for index, value in frag1_start.items():
    key = value
    if key in dict_baitmap:
        item = dict_baitmap[key]
        frag_1IDs.append(item)
        frag1_is_bait.append(True)
    else:
        frag1_is_bait.append(False)
        frag_1IDs.append("none")

frag_2IDs = []
frag2_is_bait = []
for index, value in frag2_start.items():
    key = value
    if key in dict_baitmap:
        item = dict_baitmap[key]
        frag_2IDs.append(item)
        frag2_is_bait.append(True)
    else:
        frag2_is_bait.append(False)
        frag_2IDs.append("none")


chr1 = washU_read["chr1"]
chr2 = washU_read["chr2"]
#Need to record IDs of the baits above so that I can use that to pull out the Gene name I want down below in the for loops


source_chrm = []
source_start = []
source_end = []
source_gene = []
target_chrm = []
target_start = []
target_end = []
target_gene = []
target_strand = []

for line in range(len(washU_read)):
    bait = frag1_is_bait[line]
    if bait == True:
        chrm = chr1[line]
        source_chrm.append(chrm)
        start = frag1_start[line]
        source_start.append(start)
        end = frag1_end[line]
        source_end.append(end)
        gene = frag_1IDs[line]
        source_gene.append(gene)
        t_chrm = chr2[line]
        target_chrm.append(t_chrm)
        t_start = frag2_start[line]
        target_start.append(t_start)
        t_end = frag2_end[line]
        target_end.append(t_end)
        t_bait = frag2_is_bait[line]
        if t_bait == True:
            t_gene = frag_2IDs[line]
            target_gene.append(t_gene)
            target_strand.append('+')
        else:
            target_gene.append('.')
            target_strand.append('-')

    elif bait != True:
        chrm2 = chr2[line]
        source_chrm.append(chrm2)
        start2 = frag2_start[line]
        source_start.append(start2)
        end2 = frag2_end[line]
        source_end.append(end2)
        gene = frag_2IDs[line]
        source_gene.append(gene)
        t_chrm = chr1[line]
        target_chrm.append(t_chrm)
        t_start = frag1_start[line]
        target_start.append(t_start)
        t_end = frag1_end[line]
        target_end.append(t_end)
        target_gene.append('.')
        target_strand.append('-')

       
#change to just check if the starts match!!!

#13 and 18: same as above but with '+'
name = []
ex = []
color = []
source_strand = []
for line in range(len(chrm_interaction)):
    name.append('.')
    ex.append('.')
    color.append(0)
    source_strand.append('+')


ucsc = pd.DataFrame({
    'Chrom': chrm_interaction,
    'Chrom_start': start_pos,
    'Chrom_end': end_pos,
    'col_n': name,
    'Score': scores,
    'Value': stored_strengths,
    'Ex': ex,
    'Color': color,
    'Source_chrm': source_chrm,
    'Source_start': source_start,
    'Source_end': source_end,
    'Source_name': source_gene,
    'Source_strand': source_strand,
    'target_chrm': target_chrm,
    'target_start': target_start,
    'target_end': target_end,
    'target_name': target_gene,
    'target_strand': target_strand})
#print(ucsc)

ucsc["Chrom_start"] = ucsc["Chrom_start"].astype(int)
ucsc["Chrom_end"] = ucsc["Chrom_end"].astype(int)
ucsc["Score"] = ucsc["Score"].astype(int)
ucsc["Value"] = ucsc["Value"].astype(int)
ucsc["Source_start"] = ucsc["Source_start"].astype(int)
ucsc["Source_end"] = ucsc["Source_end"].astype(int)
ucsc["target_start"] = ucsc["target_start"].astype(int)
ucsc["target_end"] = ucsc["target_end"].astype(int)

for line in range(len(ucsc)):
    values = pd.isnull(ucsc.loc[line, "Source_name"])
    if values == True:
        #print("yes working")
        new_name = "none"
        ucsc.at[line, "Source_name"] = new_name

for line in range(len(ucsc)):
    values = pd.isnull(ucsc.loc[line, "target_name"])
    if values == True:
        print("yes working")
        new_name = "none"
        ucsc.at[line, "target_name"] = new_name


with open(output_file, 'w') as file:
    file.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full\n')
ucsc.to_csv(output_file, header=False, sep='\t', index=False, mode='a')

top_i_pp_df = pd.DataFrame(columns=ucsc.columns)
top_i_pe_df = pd.DataFrame(columns=ucsc.columns)

for line in range(len(ucsc)):
    frag1 = ucsc["Source_strand"][line]
    frag2 = ucsc["target_strand"][line]
    if frag1 == "+" and frag2 == "+":
        top_i_pp_df.loc[len(top_i_pp_df)] = ucsc.iloc[line]
    elif frag1 == "+" and frag2 != "+":
        top_i_pe_df.loc[len(top_i_pe_df)] = ucsc.iloc[line]

top_i_pp_df = top_i_pp_df.sort_values(by="Score", ascending=False).head(6)
top_i_pe_df = top_i_pe_df.sort_values(by="Score", ascending=False).head(6)
top_i_pp_df.to_csv(r'pp_df.txt', index=None, sep=' ', mode='a')
top_i_pe_df.to_csv(r'pe_df.txt', index=None, sep=' ', mode='a')

print(top_i_pp_df)
print(top_i_pe_df)
