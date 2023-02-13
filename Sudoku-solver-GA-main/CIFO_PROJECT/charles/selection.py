from random import uniform, choice
from operator import attrgetter
from random import uniform, choice, choices
from operator import attrgetter

def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # Sum total fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        # Sum total fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position < spin:
                return individual

    else:
        raise Exception("No optimization specified (min or max).")


def tournament(population, size=10):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    tournament = [choice(population.individuals) for i in range(size)]
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")




def roulette_wheel(population):

    n_iterations = int(len(population))
    fitness_values = []

    for individual in range(n_iterations):
        fitness_values.append(population[individual].fitness)

    if population.optim == 'min':
        fitness_values = [1/p for p in fitness_values]

    fitness_sum = sum(fitness_values[0:len(fitness_values)])
    for individual in range(n_iterations):
        fitness_values[individual] = fitness_values[individual] / fitness_sum


    roulette_winner = choices(population, weights=fitness_values, k=1)


    return roulette_winner[0]

def ranking_selection(population):
    n_iterations = int(len(population))
    fitness_values = []

    for individual in range(n_iterations):
        fitness_values.append(population[individual].fitness)

    rank = [0] * len(fitness_values)
    if population.optim == 'min':
        for i in range(1, len(fitness_values) + 1):
            rank[fitness_values.index(max(fitness_values))] = i
            fitness_values[fitness_values.index(max(fitness_values))] = min(fitness_values) - 1

    else:
        for i in range(1, len(fitness_values) + 1):
            rank[fitness_values.index(min(fitness_values))] = i
            fitness_values[fitness_values.index(min(fitness_values))] = max(fitness_values) + 1

    rank_sum = sum(rank[0:len(rank)])
    for individual in range(n_iterations):
        rank[individual] = rank[individual] / rank_sum

    rank_winner = choices(population, weights=rank, k=1)
    return rank_winner[0]
