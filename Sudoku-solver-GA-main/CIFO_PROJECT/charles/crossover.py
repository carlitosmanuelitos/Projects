from random import randint, uniform, sample
import numpy as np
#from CIFO_PROJECT.charles.albert_atual import Individual, Population
#from CIFO_PROJECT.sudoku import get_fitness

very_easy_ =  '0 0 8 1 0 0 4 0 6 0 2 0 0 0 0 0 0 3 0 0 3 0 0 0 0 0 0 9 0 0 0 3 5 0 0 0 0 0 0 0 0 2 0 7 0 4 0 2 8 6 0 0 9 0 0 0 6 0 4 8 0 0 1 0 8 0 2 0 0 6 0 9 5 1 4 0 0 0 8 0 0'
def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1)-2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2


def cycle_co(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p2)
    # While there are still None values in offspring, get the first index of
    # None and start a "cycle" according to the cycle crossover method
    while None in offspring1:
        index = offspring1.index(None)

        val1 = p1[index]
        val2 = p2[index]

        while val1 != val2:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)

        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2[index]
                    offspring2[index] = p1[index]

    return offspring1, offspring2


def pmx_co(p1, p2):
    """Implementation of partially matched/mapped crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_points = sample(range(len(p1)), 2)
    co_points.sort()

    # dictionary creation using the segment elements from both parents
    # the dictionary will be working two ways
    keys = p1[co_points[0]:co_points[1]] + p2[co_points[0]:co_points[1]]
    values = p2[co_points[0]:co_points[1]] + p1[co_points[0]:co_points[1]]
    # segment dictionary
    segment = {keys[i]: values[i] for i in range(len(keys))}

    # empty offsprings
    o1 = [None] * len(p1)
    o2 = [None] * len(p2)

    # where pmx happens
    def pmx(o, p):
        for i, element in enumerate(p):
            # if element not in the segment, copy
            if element not in segment:
                o[i] = p[i]
            # if element in the segment, take the value of the key from
            # segment/dictionary
            else:
                o[i] = segment.get(element)
        return o

    # repeat the procedure for each offspring
    o1 = pmx(o1, p1)
    o2 = pmx(o2, p2)
    return o1, o2


def arithmetic_co(p1, p2):
    """Implementation of arithmetic crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)
    # Set a value for alpha between 0 and 1
    alpha = uniform(0, 1)
    # Take weighted sum of two parents, invert alpha for second offspring
    for i in range(len(p1)):
        offspring1[i] = p1[i] * alpha + (1 - alpha) * p2[i]
        offspring2[i] = p2[i] * alpha + (1 - alpha) * p1[i]

    return offspring1, offspring2

def two_point_crossover(p1, p2):
    len_ = len(p1)
    point1 = randint(1, len_-2)
    point2 = randint(1, len_-2)
    offspring1 = np.concatenate((p1[0:point1], p2[point1:point2], p1[point2:len_]))
    offspring2 = np.concatenate((p2[0:point1], p1[point1:point2], p2[point2:len_]))
    return offspring1, offspring2

