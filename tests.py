from test_instance_creator import create_instance
from naive_formulation import solve_exactly

graph = create_instance(8, 47112134)
print(solve_exactly(graph))