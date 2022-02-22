import numpy as np
import math
import time
import random
from itertools import combinations
from collections import defaultdict


from helpers import cliques_from_list, is_solution, neighbors
from test_instances import test_graph1, test_graph2


def greedy(adj_mat, repetitions=10):
    n = adj_mat.shape[0]
    # print(adj_mat)
    best = [x for x in range(1, n+1)]
    for r in range(repetitions):
        # print(best)
        vertices = [x for x in range(1, n+1)]
        # random.seed(1)
        random.shuffle(vertices)  # random permutation of vertices
        cliques = [0 for x in range(n)]
        sizes = defaultdict(int)  # size of each clique
        sizes[0] = n
        c = 1  # clique names
        for i in range(n):
            v = vertices[i]
            labeled = False
            # will count the size of each clique among the neighbors of v:
            neighbors_cliques = defaultdict(int)
            ret = neighbors(v, adj_mat)

            for neighbor in neighbors(v, adj_mat):
                # traverse over each neighbor of vertex and find cliques of neighbor
                neighbors_cliques[cliques[neighbor-1]] += 1
            for clique, size in neighbors_cliques.items():
                if size == sizes[clique]:
                    cliques[v-1] = clique
                    sizes[clique] += 1  # contains size of clique
                    labeled = True
                    break
                    # continue
            if not labeled:
                cliques[v-1] = c
                sizes[c] += 1
                c += 1
        if len(set(cliques)) < len(set(best)):
            best = cliques
    print(cliques)
    return best


def main():
    test_graph = test_graph2
    start_time = time.time()
    solution = cliques_from_list(greedy(test_graph))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(solution), "cliques:", solution)


if __name__ == "__main__":
    main()
