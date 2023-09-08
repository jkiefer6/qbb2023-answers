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

#print(len(generation_data))

#create a plot of allele frequency over time throughout your simulation. I.e. the X axis is the generation, the Y axis is the frequency of your allele at that generation.

x_data = []
index = 0
for value in range(len(generation_data)):
    index += 1
    x_data.append(index) 
#print(x_data)

fig, ax = plt.subplots()
ax.plot(x_data, generation_data)
ax.set_xlabel("Generations")
ax.set_ylabel("Allele Frequency")
#plt.show()


#Exercise 2:
#Run your model repeatedly (at least 30 iterations) and visualize all your allele frequency trajectories together on one plot. Remember that you can lines to a matplotlib figure using a for loop.




fig, ax = plt.subplots()
for i in range(40):
    generation_data = wright_fisher_equation(0.53, 300)
    x_data_ex2 = []
    index = 0
    for value in range(len(generation_data)):
        index += 1
        x_data_ex2.append(index) 
    ax.plot(x_data_ex2, generation_data)

plt.show()










