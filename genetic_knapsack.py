import os
import math
import numpy as np


def generate_population(size, n):
    return np.array([np.random.randint(0, 2, n) for _ in range(size)])


def fitness_score(pop, w, wt, val):
    score = np.multiply(pop, wt).sum()
    if score <= w:
        return np.multiply(pop, val).sum()
    else:
        return -1


def stop(score, pop, wt):
    pack = zip(score, pop)
    sort = sorted(pack, key=lambda x: x[0], reverse=True)
    sort = np.array(sort[0][1])
    return np.multiply(sort, wt).sum(), sort


def get_selection(score, pop):
    pack = zip(score, pop)
    sort = sorted(pack, key=lambda x: x[0], reverse=True)
    sort = np.array([j for _, j in sort[0:SELECTION_SIZE]])
    return sort


def get_crossover(pop, n):
    child = list()
    it = iter(pop)
    for i, j in zip(it, it):
        cr = np.random.rand()
        if cr > CROSSOVER_RATE:
            idx = np.random.randint(0, n)
            ch1 = list(i[0:idx]) + list(j[idx:n])
            child.append(ch1)
            ch1 = list(j[0:idx]) + list(i[idx:n])
            child.append(ch1)
        else:
            child.append(i)
            child.append(j)

    return np.array(child)


def get_mutation(pop, n):
    bits = int(math.ceil(n*MUTATION_RATE))
    for p in pop:
        #print(f"Pop : {p}")
        for _ in range(bits):
            idx = np.random.randint(0, n)
            p[idx] = 0 if p[idx] == 1 else 1
    return pop


def knapSack(w, wt, val, n):
    print("\tGenerating popullation :- 0")
    pop = generate_population(size=POPULATION_SIZE, n=n)
    for gen_num in range(1, GENERATIONS+1):
        # Calculation fitness score for each popullation.
        score = np.array([fitness_score(i, w, wt, val) for i in pop])

        # Checking to stop or not.
        stp = stop(score, pop, wt)
        if stp[0] == w:
            print(f"\t\tSolution found at generation {gen_num-1}")
            return stp[1]

        # Selection process for the current generation popullation.
        selected_pop = get_selection(score, pop)

        # Crossover proceess for selected popullation. (One- Point CrossOver)
        cross_pop = get_crossover(selected_pop, n)

        # Mutation processs for selected popullation. (Random bit flip)
        mutate_pop = get_mutation(cross_pop, n)

        # Generating new popullation.
        print(f"\tGenerating popullation :  {gen_num}")
        pop = list(generate_population(
            size=POPULATION_SIZE-len(mutate_pop), n=n))
        pop = pop + list(mutate_pop)
        pop = np.array(pop)

    return np.zeros(n,dtype=int)


def main():
    '''Entry point to the program'''

    val = list(map(int, input(
        "Enter the values for Knapsack Problem, each seperated with a space\n").split(' ')))

    wt = list(map(int, input(
        f"\nEnter the weights for {val} values, each seperated with a space\n").split(' ')))

    w = int(input("\nEnter the total weight of the Knapsack Bag :\t"))

    n = len(val)

    res =knapSack(w, wt, val, n)
    print(
        f"\n\nTotal value which the Knapsack Bag of weight {w} can hold is:\t{np.multiply(res,val).sum()}")


if __name__ == '__main__':
    os.system('clear')
    global GENERATIONS, POPULATION_SIZE, SELECTION_SIZE, CROSSOVER_RATE, MUTATION_RATE

    MUTATION_RATE = 0.1
    CROSSOVER_RATE = 0.50
    POPULATION_SIZE = 8
    SELECTION_SIZE = int(POPULATION_SIZE * 0.25)
    GENERATIONS = 50

    main()
    # print(generate_population(10,5))


'''
60 100 120
10 20 30
50

'''
'''
20 40 60 80 100
10 20 30 40 50
70

'''