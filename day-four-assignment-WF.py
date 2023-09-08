#!/usr/bin/env python

# Psuedo code for the assignment:

# Some start alllele frequency for a set population size

#Make a list to store AF

# While allele frequency is greater than zero but less than one (not fixed):
#   Get the new allele frequency for next generation
#   np.random.binomial(2*popsize, alelle freq)   only generates number of succeses
#   convert number of successes into a frequency (think about the coin flip to clarify how to do this)

#   store allele frequency in the AF list 

## Return a list of allele frequency at each time point
# Number of generations to fixation is the length of your list

import numpy as np 
import matplotlib.pyplot as plt


def wright_fisher_equation (starting_allele_freq, starting_pop_size):
    allele_frequency_for_gen = [starting_allele_freq]
    
    allele_frequency = starting_allele_freq

    while allele_frequency < 1 and allele_frequency > 0: 
        successes = np.random.binomial(2*starting_pop_size, allele_frequency)
        allele_frequency_new = successes / (2*starting_pop_size)
        allele_frequency_for_gen.append(allele_frequency_new)
        allele_frequency = allele_frequency_new
    return allele_frequency_for_gen


generation_data = wright_fisher_equation(0.53, 300)

print(len(generation_data))



