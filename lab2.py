###############################################
### CMPLXSYS425 - Evolution in silico       ###
### Lab 2                                   ###
### ####################################### ###
### IF YOU HAVEN'T LOOKED AT THE NOTEBOOKS  ###
### ON GITHUB FIRST, PLEASE DO THAT!        ###
###############################################

#pulling this over from the Jupyter notebook
import numpy as np
from matplotlib import pyplot as plt

#define our mutant frequency helper function
def mutant_freq(a_population):
    return sum(a_population)/len(a_population)

pop_size = 20
num_mutants = 5
num_generations = 10

mutation_frequency_list = []
population = np.zeros(pop_size)

for i in range(num_mutants):
    population[i] = 1

#Let's be sure to record the frequency at the beginning of time!
mutation_frequency_list.append(mutant_freq(population))

for gen in range(num_generations):
    population = np.random.choice(population, pop_size)
    print("Generation: {0}, MutFreq: {1}".format(gen+1, mutant_freq(population)))
    mutation_frequency_list.append(mutant_freq(population))

plt.plot(mutation_frequency_list)
plt.ylabel("Mutation Freq")
plt.xlabel("Generation")
plt.show()
