def create_instance(number_nodes, edge_vector):
    result = []
    for i in range(1, number_nodes):
        for j in range(i + 1, number_nodes):
            if edge_vector % 2 == 1:
                result.append((i,j))
                edge_vector = edge_vector >> 1
    return result

example_graph = create_instance(5, 8)
complete_graph = create_instance(6, pow(2,6) - 1)
print(str(complete_graph))