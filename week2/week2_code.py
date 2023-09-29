#!/usr/bin/env python

#Exercise 1:

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def simulate_coverage(coverage, genome_len, read_len, figname):
    coverage_arr = np.zeros(genome_len)
    num_reads = int(coverage * genome_len / read_len) #calculating how many reads to do
    high = genome_len - read_len
    start_positions = np.random.randint(low = 0, high = high + 1, size = num_reads) #calculating the start pos of the reads, high is exclusive
    for start in start_positions:
        coverage_arr[start: start+read_len] += 1
    #done with the simulation of the genome part of the question
    x = np.arange(0, max(coverage_arr)+1)
    sim_0cov = genome_len - np.count_nonzero(coverage_arr)
    print(f'In the simulation, there are {sim_0cov} bases with 0 coverage')
    sim_0cov_pct = 100 * sim_0cov / genome_len
    print(f'This is {sim_0cov_pct}% of the genome')
    #Get poisson
    y_poisson = stats.poisson.pmf(x, mu = coverage) * genome_len
    #Get normal distribution
    y_normal = stats.norm.pdf(x, loc = coverage, scale = np.sqrt(coverage)) * genome_len

    fig, (ax) = plt.subplots()
    ax.hist(coverage_arr, bins = x, align = 'left', label = 'Simulation')
    ax.plot(x, y_poisson, label = 'Poisson')
    ax.plot(x, y_normal, label = 'Normal')
    ax.set_xlabel('Coverage')
    ax.set_ylabel('Frequency (bp)')
    ax.legend()
    fig.tight_layout()
    fig.savefig(figname)

simulate_coverage(30, 1_000_000, 100, 'ex1-30x_cov.png')

#Exercise 2: De Bruijn graph 
reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

non_graph = []

k = 3

for read in reads:
  for i in range(len(read) - k):
     kmer1 = read[i: i+k]
     kmer2 = read[i+1: i+1+k]
     non_graph.append(f"{kmer1} -> {kmer2}")
     #non_graph.append(kmer2)
     #add f"{kmer1} -> {kmer2}" to graph

graph = set(non_graph)

f = open("edges.txt", "w")

for edge in graph:
   f.write(edge + "\n")
    















