def edge_vector_length(number_nodes):
    return int(number_nodes * (number_nodes - 1) / 2)


class Graph(object):
    def __init__(self, number_of_nodes, edge_vector):
        if pow(2, edge_vector_length(number_of_nodes)) - 1 < edge_vector:
            raise ValueError("edge vector too long for number of nodes in graph")
        self.number_nodes = number_of_nodes
        self.edge_vector = edge_vector

    def edge_list(self):
        result = []
        edge_vector_rest = self.edge_vector
        for i in range(1, self.number_nodes + 1):
            for j in range(i + 1, self.number_nodes + 1):
                if edge_vector_rest % 2 == 1:
                    result.append((i, j))
                edge_vector_rest = edge_vector_rest >> 1
        return result

