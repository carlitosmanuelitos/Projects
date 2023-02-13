import numpy as np
import statistics
from CIFO_PROJECT.charles.albert_atual import Individual, Population
from CIFO_PROJECT.shared_functions import list_flatten, repeated_by_col, repeated_by_row, repeated_by_block
from copy import deepcopy
from CIFO_PROJECT.charles.selection import fps, tournament, roulette_wheel, ranking_selection
from CIFO_PROJECT.charles.mutation import binary_mutation, swap_mutation, inversion_mutation, sudoku_mutation
from CIFO_PROJECT.charles.crossover import single_point_co, pmx_co, cycle_co, arithmetic_co, two_point_crossover
from random import random
from operator import attrgetter
import sys
sys.setrecursionlimit(100000000) # 10000 is an example, try with different values


very_easy_ =  '0 0 8 1 0 0 4 0 6 0 2 0 0 0 0 0 0 3 0 0 3 0 0 0 0 0 0 9 0 0 0 3 5 0 0 0 0 0 0 0 0 2 0 7 0 4 0 2 8 6 0 0 9 0 0 0 6 0 4 8 0 0 1 0 8 0 2 0 0 6 0 9 5 1 4 0 0 0 8 0 0'
easy =  '0 5 0 0 2 0 0 0 0 0 1 0 0 8 7 0 0 0 0 3 4 0 0 0 0 0 9 0 0 0 0 1 0 0 3 7 0 0 8 0 0 5 0 0 2 3 0 2 7 6 0 0 1 0 0 0 9 0 0 0 8 0 1 7 0 0 6 0 0 0 4 0 0 6 0 2 0 0 0 0 0'
moderate = '2 0 0 8 0 0 0 0 0 0 8 4 0 3 5 0 0 9 1 0 0 0 2 0 4 0 0 0 0 0 7 0 9 0 3 0 3 0 8 0 0 6 0 0 0 0 0 1 0 0 0 0 6 8 0 5 0 3 0 0 6 1 0 0 0 0 0 0 0 0 0 5 0 1 6 0 9 0 7 0 0'
hard =  '0 0 0 0 0 0 7 0 8 0 0 2 0 6 0 0 4 0 0 0 4 0 1 0 0 6 2 5 0 1 0 0 0 0 8 0 0 6 0 8 0 9 0 0 4 0 3 0 0 0 0 5 0 0 0 0 0 6 0 0 0 0 0 0 5 0 0 3 0 0 0 0 0 0 0 0 0 2 0 0 9'


#cues_list = [very_easy_, easy, moderate, hard]

def make_matrix(cues):
    cues = cues.split(' ')
    cues = ''.join(cues)
    cues = np.array(list(map(int, cues)))
    cues = cues.reshape((9,9))
    given_index = np.where(cues != 0)
    given_index = list(zip(given_index[0],given_index[1]))
    to_fill_index = np.where(cues == 0)
    to_fill_index = list(zip(to_fill_index[0],to_fill_index[1]))
    return cues, given_index, to_fill_index



#(very_easy,ve_cues, ve_to_fill), (easy,easy_cues,easy_to_fill), (moderate,moderate_cues, moderate_to_fill), \
#(hard,hard_cues, hard_to_fill) = [make_matrix(i) for i in cues_list]



def entry_fitness(entry_index, matrix, given_index):
    row_count, row_fitness = repeated_by_row(matrix)
    column_count, column_fitness = repeated_by_col(matrix)
    block_count, block_fitness = repeated_by_block(matrix)
    fitness_entry_row = 0
    fitness_entry_column = 0
    fitness_entry_block = 0
    if entry_index in given_index:
        pass
    else:
        for j in row_count[entry_index[0]]:
            if matrix[entry_index] == j[0]:
                fitness_entry_row += j[1]

        for h in column_count[entry_index[1]]:
            if matrix[entry_index] == h[0]:
                fitness_entry_column += h[1]


        counter = 0
        for g in range(0, 9, 3):
            for h in range(0, 9, 3):

                if (entry_index == (g,h)) | (entry_index == (g,h+1)) | (entry_index == (g,h+2)) | \
                (entry_index == (g+1, h)) | (entry_index == (g+1,h+1)) | (entry_index == (g+1,h+2)) | \
                (entry_index == (g+2, h)) | (entry_index == (g+2,h+1)) | (entry_index == (g+2,h+2)):
                    for k in block_count[counter]:
                        if matrix[entry_index] == k[0]:
                            fitness_entry_block += k[1]
                counter += 1
    entry_fitness = (fitness_entry_column + fitness_entry_row + fitness_entry_block)

    return entry_fitness

#Monkey Patching
Individual.entry_fitness = entry_fitness

def get_fitness(self):
    fitness_individual = []
    indexes = [(i, j) for i in range(9) for j in range(9)]
    for index in indexes:
        if index in self.given_index:
            pass
        else:
            fitness_individual.append(entry_fitness(index,self.representation, self.given_index))
    fit = sum(fitness_individual)
    return fit

def get_fitness(self):
    row_counts, row_fitness = repeated_by_row(self.representation)
    col_counts, col_fitness = repeated_by_col(self.representation)
    block_counts, block_fitness = repeated_by_block(self.representation)
    fit = (row_fitness + block_fitness + col_fitness)/3
    return fit

#Monkey Patching
Individual.get_fitness = get_fitness

if __name__ == '__main__':
    Pop = Population(size = 1000, optim="min", cues = hard)
    Pop.evolve(1000,select=ranking_selection, crossover = single_point_co, mutate= swap_mutation, co_p=0.6, mu_p=0.14,
             elitism=True, cues = hard)

