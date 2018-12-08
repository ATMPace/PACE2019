from greedy_cover import cover_greedily
from gurobipy import *


def add_variable_to_model_if_necessary(v, model, added):
    if added.__contains__(v):
        return model.getVarByName(str(v))
    added.add(v)
    added_var = model.addVar(obj=1, vtype=GRB.BINARY, name=str(v))
    model.update()
    return added_var


def read_solution(model):
    result = []
    vars_in_model = model.getVars()

    for var in vars_in_model:
        if var.X == 1:
            result.append(var.VarName)
    result.sort()
    return result


def add_constraints_to_model(edges, model):
    added = set()
    for edge in edges:
        (u, v) = edge
        var_u = add_variable_to_model_if_necessary(u, model, added)
        var_v = add_variable_to_model_if_necessary(v, model, added)
        model.addConstr(var_u + var_v >= 1)


def solve_exactly(graph, create_start_solution=True):
    model = Model("vertex_cover_IP")
    model.setParam("MIPGap", 0)
    add_constraints_to_model(graph.edge_list(), model)
    if create_start_solution:
        initial_solution = cover_greedily(graph)
        for initial_var in initial_solution:
            model.getVarByName(str(initial_var)).start = 1
    model.update()
    model.optimize()
    return read_solution(model)
