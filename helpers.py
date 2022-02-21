import numpy as np
from itertools import combinations
import os


def neighbors(nodes, adj_mat):
    '''Takes one or a list of nodes (each one between 1 and N) and returns its neighbors (between 1 and N)'''
    # print(adj_mat)
    neighbors = set()
    neighbor = adj_mat[nodes-1]
    count = 0
    for i in neighbor:
        count = count + 1
        if(i == 1):
            neighbors.add(count)
    return neighbors


def is_clique(nodes, adj_mat):
    for (node_i, node_j) in combinations(nodes, 2):
        if not is_edge(node_i, node_j, adj_mat):
            return False
    return True


def is_edge(u, v, adj_mat):
    return adj_mat[u-1, v-1] or adj_mat[v-1, u-1]


def is_solution(nodes_list, adj_mat, v=None):
    "Verifies if the cliques in x up to v are indeed cliques"
    if v is None:
        v = adj_mat.shape[0]
    cliques_dict = cliques_from_list(nodes_list, v)
    for clique_nodes in cliques_dict.values():
        if not is_clique(clique_nodes, adj_mat):
            return False
    return True


def cliques_from_list(nodes_list, v=None):
    '''Takes the list X = [1 1 2 3 3 ... ] of nodes containing the label of their associated clique, and returns a dict of the different cliques'''
    if v is None:
        v = len(nodes_list)
    cliques = dict()
    for i in range(v):
        clique = nodes_list[i]
        if clique == 0:
            continue
        if clique in list(cliques):
            cliques[clique].add(i+1)
        else:
            cliques[clique] = set([i+1])

    return cliques
