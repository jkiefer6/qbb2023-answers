#!/usr/bin/env python

import numpy as np 
import sys
from fasta import readFASTA
import pandas as pd 
"""
fasta_file = sys.argv[1]
#could do it this way but i actually hate typing in the command line
"""
def my_file_opener(fasta_file, scoring_matrix_file, gap_penalty):
    input_sequences = readFASTA(open(fasta_file))
    seq1_id, sequence1 = input_sequences[0]
    seq2_id, sequence2 = input_sequences[1]
    scoring_matrix = pd.read_csv(scoring_matrix_file, delim_whitespace=True)
    return scoring_matrix, sequence1, sequence2, seq1_id, seq2_id, gap_penalty 

scoring_matrix, sequence1, sequence2, seq1_id, seq2_id, gap_penalty = my_file_opener("CTCF_38_M27_AA.faa", "HOXD70.txt", -10)


F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
traceback_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

"""
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i * gap_penalty
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty

for i in range(1, F_matrix.shape[0]):
    for j in range(1, F_matrix.shape[1]):
        if sequence1[i-1] == sequence2[j-1]:
            d = F_matrix[i-1, j-1] + match_score
        else:
            d = F_matrix[i-1, j-1] + mismatch_score
        
        h = F_matrix[i, j-1] + gap_penalty
        v = F_matrix[i-1, j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)

print(F_matrix)
"""

