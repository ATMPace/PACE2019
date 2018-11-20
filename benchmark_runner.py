from test_instance_creator import create_random_graph
import time
from naive_formulation import solve_exactly


def run_benchmark(algorithm_reference, algorithm_to_test, number_of_start_nodes, node_increase_per_iteration, iterations):
    difference_per_iteration = []
    for iter in range(iterations):
        number_of_nodes = number_of_start_nodes + node_increase_per_iteration * iter
        graph = create_random_graph(number_of_nodes)
        duration_reference = AlgorithmRunner(algorithm_reference).run(graph)
        duration_algorithm_to_test = AlgorithmRunner(algorithm_to_test).run(graph)
        difference_per_iteration.append((duration_reference - duration_algorithm_to_test, duration_algorithm_to_test / duration_reference))
    sums = (0,0)
    for pair in difference_per_iteration:
        p1, p2 = pair
        s1, s2 = sums
        sums = (s1 + p1, s2 + p2)
    sum_absolutes, sum_relatives = sums
    mean_absolute = sum_absolutes / iterations
    mean_relative = sum_relatives / iterations
    print("result")
    print("======")
    print("iteration differences: " + str(difference_per_iteration))
    print("mean absolute difference: " + str(mean_absolute))
    print("mean relative deviation: " + str(mean_relative))


class AlgorithmRunner(object):
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def run(self, edge_list):
        clock_before = time.time()
        self.algorithm(edge_list)
        clock_after = time.time()
        run_time = clock_after - clock_before
        return run_time


# definition of algorithms to benchmark
def solve_exactly_with_greedy(edge_list):
    solve_exactly(edge_list, create_start_solution=True)


def solve_exactly_without_greedy(edge_list):
    solve_exactly(edge_list, create_start_solution=False)


# let's see what the performance gain of the greedy algorithm is
run_benchmark(solve_exactly_without_greedy, solve_exactly_with_greedy, 100, 25, 20)