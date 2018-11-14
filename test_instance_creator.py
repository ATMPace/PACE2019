def edge_vector_length(number_nodes):
    return int(number_nodes * (number_nodes - 1) / 2)


def create_instance(number_of_nodes, edge_vector):
    if pow(2, edge_vector_length(number_of_nodes)) - 1 < edge_vector:
        raise ValueError("edge vector too long for number of nodes in graph")
    result = []
    edge_vector_rest = edge_vector
    for i in range(1, number_of_nodes + 1):
        for j in range(i + 1, number_of_nodes + 1):
            if edge_vector_rest % 2 == 1:
                result.append((i,j))
            edge_vector_rest = edge_vector_rest >> 1
    return result


# example usages
# example_graph = create_instance(4, 15)
# print("example 1: " + str(example_graph))

# number_of_nodes = 6
# complete_graph = create_instance(number_of_nodes, pow(2, edge_vector_length(number_of_nodes)) - 1)
# print("example 2: " + str(complete_graph))
