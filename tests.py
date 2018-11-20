from test_instance_creator import *
from naive_formulation import solve_exactly
import benchmark_runner


# solve one instance
graph = create_random_graph(number_of_nodes = 200)

print("random graph is " + str(graph))
print(solve_exactly(graph))

# benchmark of naive formulation with and without greedy start solution
benchmark_runner.run_benchmark()