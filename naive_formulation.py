from greedy_cover import cover_greedily
from gurobipy import *


def add_variable_to_model_if_necessary(v, model, added):
    if added.__contains__(v):
        return
    added.add(v)
    model.addVar(obj=1, vtype=GRB.BINARY, name=str(v))
    return


def read_solution(model):
    result = set()
    vars_in_model = model.getVars()

    for var in vars_in_model:
        if var.X == 1:
            result.add(var.name)
    return result


def add_constraints_to_model(edges, model):
    added = set()
    for edge in edges:
        (u, v) = edge
        add_variable_to_model_if_necessary(u, model, added)
        add_variable_to_model_if_necessary(v, model, added)
        var_u = model.getVarByName(str(u))
        var_v = model.getVarByName(str(v))
        model.addConstr(vars.sum(var_u, var_v) >= 1)


def solve_exactly(edgelist):
    initial_solution = cover_greedily(edgelist)
    model = Model("vertex_cover_IP")
    model.setParam("MIPGap", 0)
    for initial_var in initial_solution:
        model.getVarByName(str(initial_var)).start = 1
    add_constraints_to_model(edgelist, model)
    model.optimize()
    return read_solution(model)


edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 4), (3, 1), (3, 2), (6, 1), (8, 0), (1, 8)]
print("input graph as edge list:" + str(edges))
solution = solve_exactly(edges)
print("optimal solution " + str(solution))
