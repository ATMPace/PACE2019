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


def from_gr_format(graph):
    split = graph.split("\n")
    header = split[0]
    header_split = header.split(" ")
    number_of_nodes = int(header_split[2])
    split.pop(0)
    body = split
    edge_set = set()
    for line in body:
        edge = line.split(" ")
        if len(edge) != 2:
            continue
        u = int(edge[0])
        v = int(edge[1])
        if u < v:
            edge_set.add((u,v))
        else:
            if v > u:
                edge_set.add((v, u))
            else:
                raise ValueError("no loops allowed.")
    edge_vector = []
    for i in range(1, number_of_nodes + 1):
        for j in range(i + 1, number_of_nodes + 1):
            if edge_set.__contains__((i,j)):
                edge_vector.append(1)
            else:
                edge_vector.append(0)
    edge_vector.reverse()
    bitstring = 0
    for v in edge_vector:
        bitstring = bitstring << 1
        bitstring += v
    return Graph(number_of_nodes, bitstring)


def read_from_gr_file(file_name):
    file = open(file_name + ".gr", "r")
    contents = file.read()
    file.close()
    return from_gr_format(contents)


# example usages
# example_graph = create_instance(4, 15)
# print("example 1: " + str(example_graph))

# number_of_nodes = 6
# complete_graph = create_instance(number_of_nodes, pow(2, edge_vector_length(number_of_nodes)) - 1)
# print("example 2: " + str(complete_graph))
