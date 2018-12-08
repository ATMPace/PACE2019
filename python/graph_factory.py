from random import randint
from vc_graph import Graph, edge_vector_length

def create_random_graph(number_of_nodes):
    edge_list_vector = randint(0, pow(2, edge_vector_length(number_of_nodes)) - 1)
    return Graph(number_of_nodes, edge_list_vector)

# example usages
# example_graph = create_instance(4, 15)
# print("example 1: " + str(example_graph))

# number_of_nodes = 6
# complete_graph = create_instance(number_of_nodes, pow(2, edge_vector_length(number_of_nodes)) - 1)
# print("example 2: " + str(complete_graph))
