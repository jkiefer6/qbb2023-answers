#!/usr/bin/env python

import numpy as np 
import sys
from fasta import readFASTA
import pandas as pd 

#def my_alignment_function = (fasta_file, scoring_matrix_file, gap_penalty, write_file_name)
input_sequences = readFASTA(open("CTCF_38_M27_AA.faa"))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

scoring_matrix = pd.read_csv("BLOSUM62.txt", delim_whitespace=True)

