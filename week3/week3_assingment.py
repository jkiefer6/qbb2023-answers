#!/usr/bin/env python

import numpy as np 
import sys
from fasta import readFASTA
import pandas as pd 
"""
fasta_file = sys.argv[1] etc. 
#could do it this way but i actually hate typing in the command line
"""
"""
def my_file_opener(fasta_file, scoring_matrix_file, gap_penalty):
    input_sequences = readFASTA(open(fasta_file))
    seq1_id, sequence1 = input_sequences[0]
    seq2_id, sequence2 = input_sequences[1]
    scoring_matrix = pd.read_csv(scoring_matrix_file, delim_whitespace=True)
    return scoring_matrix, sequence1, sequence2, seq1_id, seq2_id, gap_penalty 


scoring_matrix, sequence1, sequence2, seq1_id, seq2_id, gap_penalty = my_file_opener("CTCF_38_M27_AA.faa", "BLOSUM62.txt", -10)
"""
#Opening with sys.argv
fasta_file = sys.argv[1]
scoring_matrix_file = sys.argv[2]
gap_penalty_string = sys.argv[3]

input_sequences = readFASTA(open(fasta_file))
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
scoring_matrix = pd.read_csv(scoring_matrix_file, delim_whitespace=True)
gap_penalty = float(gap_penalty_string)

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
traceback_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1), str)
traceback_matrix[0:] = "horizontal"
traceback_matrix[:,0] = "vertical"
traceback_matrix[0,0] = "star"

for i in range(len(sequence1)+1):
    F_matrix[i,0] = i * gap_penalty
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty


for i in range(1, F_matrix.shape[0]):
    for j in range(1, F_matrix.shape[1]): 
         match_score = scoring_matrix.loc[sequence1[i-1], sequence2[j-1]]
         d = F_matrix[i-1, j-1] + match_score
        
         h = F_matrix[i, j-1] + gap_penalty
         v = F_matrix[i-1, j] + gap_penalty

         F_matrix[i,j] = max(d,h,v)
         if F_matrix[i, j] == d:
            traceback_matrix[i, j] = "diagonal"
         elif F_matrix[i, j] == h:
            traceback_matrix[i, j] = "horizontal"
         else: 
            traceback_matrix[i, j] = "vertical"


#need to select optimal alignment now using a while loop


i = int(traceback_matrix.shape[0]-1)
j = int(traceback_matrix.shape[1]-1) #telling while loop to start in bottom corner

sequence_1 = []
sequence_2 = []


while i > 0 or j > 0: 
    if traceback_matrix[i, j] == "d":
        sequence_1.append(sequence1[i-1]) #telling it which letter to pull from the sequence
        sequence_2.append(sequence2[j-1])
        i = i - 1
        j = j - 1
    elif traceback_matrix[i, j] == "v":
        sequence_1.append(sequence1[i-1])
        sequence_2.append('-')
        i = i - 1
    elif traceback_matrix[i, j] == "h":
        sequence_1.append('-')
        sequence_2.append(sequence2[j-1]) 
        j = j - 1
    else: #my top position is called star
        print("weird things happening")
        i = i - 1
        j = j - 1


score = F_matrix[F_matrix.shape[0]-1, F_matrix.shape[1]-1]

seq1_GAP = sequence_1.count('-')
seq2_GAP = sequence_2.count('-')

print(score, seq1_GAP, seq2_GAP)


#Now I have to flip the sequences since they were added in the backwards order

forward_seq_1 = list(reversed(sequence_1))
forward_seq_2 = list(reversed(sequence_2))



f = open("protein_sequence_alignment.txt", "w")
f.write("Sequence 1:")
for letter in forward_seq_1:
    f.write(letter)
f.write("Sequence 2:")
for values in forward_seq_2:
    f.write(values)

"""
#Turning into a function:
def my_nw (sequence1, sequence2, scoring_matrix, gap_penalty, filename):
    F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
    traceback_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1), str)
    traceback_matrix[0:] = "horizontal"
    traceback_matrix[:,0] = "vertical"
    traceback_matrix[0,0] = "star"

    for i in range(len(sequence1)+1):
        F_matrix[i,0] = i * gap_penalty
    for j in range(len(sequence2)+1):
        F_matrix[0,j] = j * gap_penalty


    for i in range(1, F_matrix.shape[0]):
        for j in range(1, F_matrix.shape[1]): 
            match_score = scoring_matrix.loc[sequence1[i-1], sequence2[j-1]]
            d = F_matrix[i-1, j-1] + match_score
        
            h = F_matrix[i, j-1] + gap_penalty
            v = F_matrix[i-1, j] + gap_penalty

            F_matrix[i,j] = max(d,h,v)
            if F_matrix[i, j] == d:
                traceback_matrix[i, j] = "diagonal"
            elif F_matrix[i, j] == h:
                traceback_matrix[i, j] = "horizontal"
            else: 
                traceback_matrix[i, j] = "vertical"

    i = int(traceback_matrix.shape[0]-1)
    j = int(traceback_matrix.shape[1]-1) #telling while loop to start in bottom corner

    sequence_1 = []
    sequence_2 = []


    while i > 0 or j > 0: 
        if traceback_matrix[i, j] == "d":
            sequence_1.append(sequence1[i-1]) #telling it which letter to pull from the sequence
            sequence_2.append(sequence2[j-1])
            i = i - 1
            j = j - 1
        elif traceback_matrix[i, j] == "v":
            sequence_1.append(sequence1[i-1])
            sequence_2.append('-')
            i = i - 1
        elif traceback_matrix[i, j] == "h":
            sequence_1.append('-')
            sequence_2.append(sequence2[j-1]) 
            j = j - 1
        else: #my top position is called star
            print("weird things happening")
            i = i - 1
            j = j - 1

    score = F_matrix[F_matrix.shape[0]-1, F_matrix.shape[1]-1]

    seq1_GAP = sequence_1.count('-')
    seq2_GAP = sequence_2.count('-')

    #Now I have to flip the sequences since they were added in the backwards order

    forward_seq_1 = list(reversed(sequence_1))
    forward_seq_2 = list(reversed(sequence_2))

    f = open("filename", "w")
    f.write("Sequence 1:")
    for letter in forward_seq_1:
        f.write(letter)
    f.write("Sequence 2:")
    for values in forward_seq_2:
        f.write(values)
    return score, seq1_GAP, seq2_GAP

score, seq1_GAP, seq2_GAP = my_nw(sequence1, sequence2, scoring_matrix, -10, "protein_sequence_alignment.txt")
print(score, seq1_GAP, seq2_GAP)
"""
