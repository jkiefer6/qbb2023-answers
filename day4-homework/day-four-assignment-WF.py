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
plt.show()
fig.savefig( "Generations_vs_AlleleFrequency" )
plt.close(fig)

#Exercise 2:
#Run your model repeatedly (at least 30 iterations) and visualize all your allele frequency trajectories together on one plot. Remember that you can lines to a matplotlib figure using a for loop.


"""

fig, ax = plt.subplots()
for i in range(40):
    generation_data = wright_fisher_equation(0.53, 300)
    x_data_ex2 = []
    index = 0
    for value in range(len(generation_data)):
        index += 1
        x_data_ex2.append(index) 
    ax.plot(x_data_ex2, generation_data)

#plt.show()

#Pt. 2 - run model 1000 times and create a histogram (dot hist) of time to fixation

time_to_fix = []
for i in range(1000):
    generation_data = wright_fisher_equation(0.53, 300)
    time_to_fix.append(len(generation_data))

fig, ax = plt.subplots()
ax.hist(time_to_fix)
#plt.show()


#Exercise 3:

#my pop sizes: 50, 100, 150, 200, 250

def my_mean(integer_list):
    total = []
    assert type (integer_list[0]) in [int], "make data an integer"
    for value in range(len(integer_list)):
        total.append(integer_list[value])
    final = sum(total)
    average = final / len(integer_list)
    return average



time_to_fix = []
for i in range(1000):
    generation_data = wright_fisher_equation(0.53, 50)
    time_to_fix.append(len(generation_data))
avg_fix_50 = my_mean(time_to_fix)


time_to_fix = []
for i in range(1000):
    generation_data = wright_fisher_equation(0.53, 100)
    time_to_fix.append(len(generation_data))
avg_fix_100 = my_mean(time_to_fix)

time_to_fix = []
for i in range(1000):
    generation_data = wright_fisher_equation(0.53, 150)
    time_to_fix.append(len(generation_data))
avg_fix_150 = my_mean(time_to_fix)

time_to_fix = []
for i in range(1000):
    generation_data = wright_fisher_equation(0.53, 200)
    time_to_fix.append(len(generation_data))
avg_fix_200 = my_mean(time_to_fix)

time_to_fix = []
for i in range(1000):
    generation_data = wright_fisher_equation(0.53, 250)
    time_to_fix.append(len(generation_data))
avg_fix_250 = my_mean(time_to_fix)


x_data_2 = [50, 100, 150, 200, 250]
y_data = [avg_fix_50, avg_fix_100, avg_fix_150, avg_fix_200, avg_fix_250]

fig, ax = plt.subplots()
ax.plot(x_data_2, y_data)
ax.set_xlabel("Population Size")
ax.set_ylabel("Avergae Time to Fixation")
#plt.show()

#Pt. 2

time_to_fix = []
for i in range(10):
    generation_data = wright_fisher_equation(0.1, 1000)
    time_to_fix.append(len(generation_data))
avg_fix_010 = my_mean(time_to_fix)


time_to_fix = []
for i in range(10):
    generation_data = wright_fisher_equation(0.3, 1000)
    time_to_fix.append(len(generation_data))
avg_fix_030 = my_mean(time_to_fix)

time_to_fix = []
for i in range(10):
    generation_data = wright_fisher_equation(0.5, 1000)
    time_to_fix.append(len(generation_data))
avg_fix_050 = my_mean(time_to_fix)

time_to_fix = []
for i in range(10):
    generation_data = wright_fisher_equation(0.7, 1000)
    time_to_fix.append(len(generation_data))
avg_fix_070 = my_mean(time_to_fix)

time_to_fix = []
for i in range(10):
    generation_data = wright_fisher_equation(0.9, 1000)
    time_to_fix.append(len(generation_data))
avg_fix_090 = my_mean(time_to_fix)


x_data_3 = [0.10, 0.30, 0.50, 0.70, 0.90]
y_data_2 = [avg_fix_010, avg_fix_030, avg_fix_050, avg_fix_070, avg_fix_090]

fig, ax = plt.subplots()
ax.plot(x_data_3, y_data_2)
ax.set_xlabel("Starting Allele Frequency")
ax.set_ylabel("Avergae Time to Fixation")
plt.show()


question 1 : Understanding the plot of pop size vs allele frequency
    In this plot, as population size increases along the x axis, average time to fixation
    also increases. This makes sense because as number of individuals
    increases, the number of chromosomes also increases. Therefore, in order for genetic drift
    to be "achieved", more alleles have to be changed to reach fixation. Therefore, more genertations
    are required for these alleles to become fixed. So then, average time to fixation increases
    along with population size. 

question 2 : Changing the assumptions of W-F model (constant pop size)
    The Wright-Fisher model, the model assumes that population size remains constant. If population
    size changed every generation, then time to fixation would liekly shift as well. Within the model
    changing population size, increased time to fixation. This suggests then that if pop size shifted
    every generation, if the pop size increased, time to fixation would also increase. Inversely, if the 
    population died off, then time to fixation would decrease. Therefore, a model that allows for 
    some variability in pop size, would also see more dynamic changes in time to fixation. Nature 
    violates the constant population size all of the time. Not every individual reproduces in every generation 
    and populations can expereince  catalysmic events (fire, flood, etc.) that may result in a dramatic reduction of 
    individuals. If a population experienced this, the time for fixation for a specific allele 
    would be much accleerated when compared to the population before such an event. 
Question 3 : Changing the assumptions of W-F model (random mating)
    The Wright-Fisher model assumes that mating between individuals is random. However in nature most of the time,
    mating is not random. But rather mates are selected according to traits that make them more attarctive to other
    organisms or traits that allow them to live longer than their peers. For example, if an allele increased the 
    ability of an organism to survive (ie better hunting or better blending in to surroundings) then this organism
    has a greater probabilty of surviving to aduthood and passing on their alleles. This would in turn affect the 
    time to fixation for a specific allele. If mates with the allele were favored over those without, 
    the time to fixation would decrease as mates with the allele would preferentially be able to pass on their 
    alleles increasing the frequency of the allele in the next populations. The inverse would also be true. 

#Adv Exercise 1

def wright_fisher_equation_selection (starting_allele_freq, starting_pop_size, selection_coefficient):
    allele_frequency_for_gen = [starting_allele_freq]
    allele_frequency = starting_allele_freq

    while allele_frequency < 1 and allele_frequency > 0: 
        val_i = allele_frequency * (2*starting_pop_size)
        #print(val_i)
        top = val_i * (1 + selection_coefficient)
        bottom = 2*starting_pop_size - val_i + (val_i * (1 + selection_coefficient))
        prob = top / bottom
        successes = np.random.binomial(2*starting_pop_size, prob)
        allele_frequency_new = successes / (2*starting_pop_size)
        allele_frequency_for_gen.append(allele_frequency_new)
        allele_frequency = allele_frequency_new
    return allele_frequency_for_gen


#generation_data = wright_fisher_equation_selection(0.53, 300, 0.01)
#print(len(generation_data))

x_data_A = []
index = 0
for value in range(len(generation_data)):
    index += 1
    x_data_A.append(index) 
#print(x_data)

fig, ax = plt.subplots()
ax.plot(x_data_A, generation_data)
ax.set_xlabel("Generations")
ax.set_ylabel("Allele Frequency")
plt.show()

#With diff s = 0.02
generation_data = wright_fisher_equation_selection(0.53, 300, 0.02)
x_data_B = []
index = 0
for value in range(len(generation_data)):
    index += 1
    x_data_B.append(index) 
#print(x_data)

fig, ax = plt.subplots()
ax.plot(x_data_B, generation_data)
ax.set_xlabel("Generations")
ax.set_ylabel("Allele Frequency")
plt.show()



#Q: Introducing a selection coefficient makes the allele much more likely to reach fixation where all 
#individuals have the allele in a shorter time frame. 

#Adv Ex 2:
#pop size list
def my_mean(integer_list):
    total = []
    assert type (integer_list[0]) in [int], "make data an integer"
    for value in range(len(integer_list)):
        total.append(integer_list[value])
    final = sum(total)
    average = final / len(integer_list)
    return average

pop_sizes = np.arange(1000, 10000, 1000).tolist()
allele_freq = np.arange(0.1, 1, 0.1).tolist()

avg_fix_time = []
len_of_gen = []


index = 0
for value in pop_sizes:
    starting_pop_size_mod = pop_sizes[index]
    starting_allele_freq_mod = allele_freq[index]
    for i in range(10):
        generation_data = wright_fisher_equation_selection(starting_allele_freq = starting_allele_freq_mod, starting_pop_size = starting_pop_size_mod, selection_coefficient = 0)
        len_of_gen.append(len(generation_data))
        index = index +1
    avg_fix_time.append(my_mean(len_of_gen))

#print(len_of_gen)

print(len(avg_fix_time))

#data = np.random.random(( 12 , 12 ))

#plt.imshow(avg_fix_time)
 
#plt.title( "Average Fixation Time" )
#plt.show()

x = pop_sizes = np.arange(1000, 10000, 1000)
y = allele_freq = np.arange(0, 1, 0.1)
z = np.arange(avg_fix_time)
cols = np.unique(x).shape[0]
X = x.reshape(-1, cols)
Y = y.reshape(-1, cols)
Z = z.reshape(-1, cols)
plt.contourf(X,Y,Z)
plt.show()
"""