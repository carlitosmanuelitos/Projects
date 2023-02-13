import random
from random import randint, sample, choice
import numpy as np
from CIFO_PROJECT.shared_functions import list_flatten, repeated_by_col, repeated_by_row, repeated_by_block

def binary_mutation(individual):
    """Binary mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary.")

    return individual


def swap_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(range(len(individual)), 2)
    # Swap them
    individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]

    return individual


def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Position of the start and end of substring
    mut_points = sample(range(len(individual)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    individual[mut_points[0]:mut_points[1]] = individual[mut_points[0]:mut_points[1]][::-1]

    return individual

def sudoku_mutation(ind):
    mut_point = choice(ind.to_fill_index)
    row_count, row_fitness = repeated_by_row(ind.representation)
    column_count, column_fitness = repeated_by_col(ind.representation)
    block_count, block_fitness = repeated_by_block(ind.representation)
    fitness_entry_row = 0
    fitness_entry_column = 0
    fitness_entry_block = 0
    possible_row = [i for i in range(1, 10)]
    possible_column = [i for i in range(1, 10)]
    possible_block = [i for i in range(1, 10)]
    for j in row_count[mut_point[0]]:
        possible_row.remove(j[0])

    for h in column_count[mut_point[1]]:
        possible_column.remove(h[0])

    counter = 0
    for g in range(0, 9, 3):
        for h in range(0, 9, 3):
            if (mut_point == (g, h)) | (mut_point == (g, h + 1)) | (mut_point == (g, h + 2)) | \
                    (mut_point == (g + 1, h)) | (mut_point == (g + 1, h + 1)) | (
                    mut_point == (g + 1, h + 2)) | \
                    (mut_point == (g + 2, h)) | (mut_point == (g + 2, h + 1)) | (
                    mut_point == (g + 2, h + 2)):
                for k in block_count[counter]:
                    possible_block.remove(k[0])
            counter += 1
    possible_values = [0,1,2,3,4,5,6,7,8,9]
    for i in possible_values:
        if i not in possible_block:
            possible_values.remove(i)
    for i in possible_values:
        if i not in possible_row:
            possible_values.remove(i)
    for i in possible_values:
        if i not in possible_column:
            possible_values.remove(i)

    print('mut point', mut_point, 'possible values', possible_values, '\nrepresentation\n', ind.representation)
    for i in ind.to_fill_index:
        if i == mut_point:
            change_index = ind.to_fill_index.index(i)
    ind.fill_values[change_index] = random.choice(possible_values)


    return ind



if __name__ == '__main__':
    test = [6, 1, 3, 5, 2, 4, 7]
    test = inversion_mutation(test)
    #print([i for i in range(1, 10)])
