import sys
from collections import OrderedDict

# Test graphs.
input_graph_1 = {
    0: [(7, 8), (1, 4)],
    1: [(0, 4), (2, 8)],
    7: [(0, 8), (8, 7), (6, 1)],
    2: [(1, 8), (8, 2), (5, 4), (3, 7)],
    8: [(7, 7), (6, 6), (2, 2)],
    6: [(7, 1), (5, 2), (8, 6)],
    3: [(2, 7), (4, 9), (5, 14)],
    5: [(2, 4), (3, 14), (4, 10)],
    4: [(3, 9), (5, 10)]
}

input_graph_2 = {
    0: [(1, 5), (2, 1)],
    1: [(0, 5), (2, 3)],
    2: [(0, 1), (1, 3)]
}

# Graph provided for the assignment.
assignment_graph = {
    6: [(1, 10), (5, 25)],
    1: [(2, 28), (6, 10)],
    5: [(7, 24), (4, 22), (6, 25)],
    7: [(5, 24), (4, 18), (2, 14)],
    2: [(7, 14), (1, 28), (3, 16)],
    4: [(7, 18), (5, 22), (3, 12)],
    3: [(2, 16), (4, 12)]
}


# Implementation of Prims Algorithm
def prims_algorithm(test_graph):
    mst_set = OrderedDict()
    node_dict = {}

    node = None
    for node in test_graph:
        node_dict[node] = sys.maxsize
    node_dict[node] = 0

    while True:
        min_node = get_min_node_not_visited(node_dict, mst_set)

        if min_node is None:
            return print_ordered_dict(mst_set), get_weight_of_minimum_spanning_tree(node_dict)

        mst_set[min_node] = "Visited"
        for connected_node, weight in test_graph[min_node]:
            if connected_node not in mst_set:
                if weight < node_dict[connected_node]:
                    node_dict[connected_node] = weight


# Get the node with the least edge that has not been visited
def get_min_node_not_visited(node_dict, visited_nodes):
    min_node = None
    min_value = sys.maxsize

    for node in node_dict:
        if node not in visited_nodes:
            if node_dict[node] < min_value:
                min_value = node_dict[node]
                min_node = node

    return min_node


# helper functions
# Get list of selected nodes in order.
def print_ordered_dict(mst_set):
    output_array = []

    for node in mst_set:
        output_array.append(node)

    return output_array


# Sum up the minimum weight of each node in the input tree.
def get_weight_of_minimum_spanning_tree(node_dict):
    accumulator = 0
    for key in node_dict:
        accumulator += node_dict[key]

    return accumulator


# Test algorithm implementation on the assignment graph provided.
print(prims_algorithm(assignment_graph))
