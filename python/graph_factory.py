from random import randint
from vc_graph import Graph, edge_vector_length


def create_random_graph(number_of_nodes):
    edge_list_vector = randint(0, pow(2, edge_vector_length(number_of_nodes)) - 1)
    return Graph(number_of_nodes, edge_list_vector)


def to_gr_format(graph):
    edge_list = graph.edge_list()
    result = "p td " + str(graph.number_nodes) + " " + str(len(edge_list)) + "\n"
    for edge in edge_list:
        (u, v) = edge
        result += str(u) + " " + str(v) + "\n"
    return result


def write_graph_to_file(file_name, graph):
    file = open(file_name + ".gr", "w")
    file.write(to_gr_format(graph))
    file.close()

# example usages
# example_graph = create_instance(4, 15)
# print("example 1: " + str(example_graph))

# number_of_nodes = 6
# complete_graph = create_instance(number_of_nodes, pow(2, edge_vector_length(number_of_nodes)) - 1)
# print("example 2: " + str(complete_graph))
