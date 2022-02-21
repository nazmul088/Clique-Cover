import time
import numpy as np
import math

from helpers import cliques_from_list, is_solution
from test_instances import test_graph1, test_graph2


def brute_force(adj_mat, cliques, v=0, best=(math.inf, None)):

    n = adj_mat.shape[0]
    # print(cliques)
    if v == n:
        if is_solution(cliques, adj_mat):
            # print(best[0])
            if len(set(cliques)) < best[0]:
                best = (len(set(cliques)), cliques_from_list(cliques))

    else:
        for i in range(1, v+2):
            # print('here', cliques)
            cliques[v] = i
            best = brute_force(adj_mat, cliques, v+1, best)
    # print(best)
    return best


def main():
    test_graph = test_graph2

    start_time = time.time()
    cliques = [0 for x in range(test_graph.shape[0])]
    cliques[0] = 1
    solution = brute_force(test_graph, cliques, 0)
    print(solution[0], "cliques:", solution[1])
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
