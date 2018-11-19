from test_instance_creator import *
from naive_formulation import solve_exactly
from random import randint

number_of_nodes = 200
random_edges = randint(0, pow(2, edge_vector_length(number_of_nodes)) - 1)
print("random edge vector is " + str(random_edges))
graph = create_instance(number_of_nodes, random_edges)
print(solve_exactly(graph))
