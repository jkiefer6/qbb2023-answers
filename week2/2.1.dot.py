#!/usr/bin/env python

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

non_graph = []

k = 3

for read in reads:
  for i in range(len(read) - k - 1):
     kmer1 = read[i: i+k]
     kmer2 = read[i+1: i+1+k]
     non_graph.append(f"{kmer1} -> {kmer2}")
     #non_graph.append(kmer2)
     #add f"{kmer1} -> {kmer2}" to graph

graph = set(non_graph)

f = open("edges.dot", "w")

f.write("digraph {")
for edge in graph:
   f.write(edge + "\n")
f.write("}")

