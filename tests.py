from test_instance_creator import create_instance
from naive_formulation import solve_exactly
from random import randint

random_edges = randint(0, pow(2, 100 * 199)-1)
print("random edge vector is " + str(random_edges))
graph = create_instance(200, random_edges)
print(solve_exactly(graph))
