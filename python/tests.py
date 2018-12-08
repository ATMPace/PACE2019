from graph_factory import *
from naive_formulation import solve_exactly
from benchmark_runner import run_benchmark

# solve one instance
graph = create_random_graph(number_of_nodes=200)

print("random graph is " + str(graph))
print("solution: " + solve_exactly(graph))


# definition of algorithms to benchmark
def solve_exactly_with_greedy(graph):
    solve_exactly(graph, create_start_solution=True)


def solve_exactly_without_greedy(graph):
    solve_exactly(graph, create_start_solution=False)


# let's see what the performance gain of the greedy algorithm is
run_benchmark(solve_exactly_without_greedy, solve_exactly_with_greedy, 100, 25, 2)
