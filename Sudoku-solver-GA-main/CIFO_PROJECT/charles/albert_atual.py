from random import shuffle, choice, sample, random, randint
from operator import attrgetter
from copy import deepcopy
import numpy as np
#from CIFO_PROJECT.sudoku import make_matrix, very_easy_
#from CIFO_PROJECT.sudoku import make_matrix, list_flatten, repeated_by_row, \
#    repeated_by_col, repeated_by_block, entry_fitness
from CIFO_PROJECT.charles.mutation import sudoku_mutation


class Individual:
    def __init__(
        self,
        i_representation=None,
        cues = None,
        fill_values = None
    ):

        self.matrix = None
        cues = cues.split(' ')
        cues = ''.join(cues)
        cues = np.array(list(map(int, cues)))
        self.cues = cues.reshape((9, 9))
        self.given_index = np.where(self.cues != 0)
        self.given_index = list(zip(self.given_index[0], self.given_index[1]))
        self.to_fill_index = np.where(self.cues == 0)
        self.to_fill_index = list(zip(self.to_fill_index[0], self.to_fill_index[1]))

        if i_representation is None:
            if fill_values is not None:
                self.fill_values = fill_values

            elif fill_values is None:
                self.fill_values = []
                for i in range(len(self.to_fill_index)):
                    self.fill_values.append(randint(1, 9))

        else:
            self.i_representation = i_representation
        self.fitness = self.get_fitness()


    @property
    def representation(self):
        rep = deepcopy(self.cues)
        for i in self.to_fill_index:
            rep[i] = self.fill_values[self.to_fill_index.index(i)]
        return rep




    #def update_rep(self, fill_values_sub):
    #    rep_copy = deepcopy(self.representation)
    #    for i in self.to_fill_index:
    #        rep_copy[i] = fill_values_sub[self.to_fill_index.index(i)]
    #        self.representation = rep_copy
    #        return self.representation




    #@representation.setter
    #def representation(self, fill_values):
    #    fill_values = self.fill_values
    #    for i in self.to_fill_index:
    #        self.representation[i] = fill_values[self.to_fill_index.index(i)]


    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")

    def entry_fitness(self):
        raise Exception("You need to monkey patch the entry fitness path.")

    #def get_neighbours(self, func, **kwargs):
    #    raise Exception("You need to monkey patch the neighbourhood function.")

    def index(self, value):
        return self.representation.index(value)

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}"


class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        for _ in range(size):
            self.individuals.append(
                Individual(
                    cues=kwargs["cues"],
                    #i_representation=kwargs["i_representation"],
                    #i_fill_values=kwargs["i_fill_values"]

                )
            )

    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism, **kwargs):
        for gen in range(gens):
            new_pop = []
            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)
                print(parent1, parent2)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1.fill_values, parent2.fill_values)
                else:
                    offspring1, offspring2 = parent1.fill_values, parent2.fill_values
                # Mutation
                if mutate == sudoku_mutation:
                    warn = 'im in mutation'
                    offspring1 = Individual(cues = kwargs["cues"], fill_values=offspring1)
                    offspring2 = Individual(cues=kwargs["cues"], fill_values=offspring2)
                    if random() < mu_p:
                        offspring1 = mutate(offspring1)
                    if random() < mu_p:
                        offspring2 = mutate(offspring2)
                    new_indiv1 = Individual(cues=kwargs["cues"], fill_values=offspring1.fill_values)
                    new_pop.append(new_indiv1)
                    if len(new_pop) < self.size:
                        new_indiv2 = Individual(cues = kwargs["cues"], fill_values=offspring2.fill_values)
                        new_pop.append(new_indiv2)
                else:
                    if random() < mu_p:
                        offspring1 = mutate(offspring1)
                    if random() < mu_p:
                        offspring2 = mutate(offspring2)
                    new_pop.append(Individual(cues=kwargs["cues"], fill_values=offspring1))
                    if len(new_pop) < self.size:
                        new_pop.append(Individual(cues=kwargs["cues"], fill_values=offspring2))

            if elitism == True:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))
                new_pop.pop(new_pop.index(least))
                new_pop.append(elite)

            self.individuals = new_pop

            if self.optim == "max":
                print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
            elif self.optim == "min":
                indiv = min(self, key=attrgetter("fitness"))
                print(f'Best Individual: \n\n {indiv.representation}')

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"





