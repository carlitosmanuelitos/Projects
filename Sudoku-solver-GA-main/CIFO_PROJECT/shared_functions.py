import numpy as np

def list_flatten(list):
    return [item for sublist in list for item in sublist]

def repeated_by_row(matrix):
    unique_counts= []
    row_fitness = 0
    for i in range(0, 9):
        unique, counts = np.unique(matrix[i], return_counts=True)
        #print('unique \n', unique)
        #print('counts \n', counts)
        unique_counts.append(np.array((unique, counts)).T)
    row_count_array = np.array(list_flatten(unique_counts))
    for i in row_count_array:
        row_fitness += (i[1] - 1)

    return unique_counts, row_fitness


def repeated_by_col(matrix):
    unique_counts=[]
    column_fitness = 0
    matrix = matrix.T
    for i in range(0, 9):
        unique, counts = np.unique(matrix[i], return_counts=True)
        #unique_counts.append(np.array(list(zip(unique, counts))))
        #unique_counts_array = np.array(flatten(column_counts_hard))
        unique_counts.append(np.asarray((unique, counts)).T)
    column_count_array = np.array(list_flatten(unique_counts))
    for i in column_count_array:
        column_fitness += (i[1]-1)

    return unique_counts, column_fitness

def repeated_by_block(matrix):
    block_fitness = 0
    block_count = []
    intermediate = []
    unique_counts = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block_count.append(matrix[i][j])
            block_count.append(matrix[i][j + 1])
            block_count.append(matrix[i][j + 2])

            block_count.append(matrix[i + 1][j])
            block_count.append(matrix[i + 1][j + 1])
            block_count.append(matrix[i + 1][j + 2])

            block_count.append(matrix[i + 2][j])
            block_count.append(matrix[i + 2][j + 1])
            block_count.append(matrix[i + 2][j + 2])

            intermediate.append(block_count)
            unique, counts = np.unique(np.array(block_count), return_counts = True)
            unique_counts.append(np.asarray((unique, counts)).T)
            block_count = []

    block_count_array = np.array(list_flatten(unique_counts))
    for i in block_count_array:
        block_fitness += (i[1]-1)

    return  unique_counts, block_fitness
