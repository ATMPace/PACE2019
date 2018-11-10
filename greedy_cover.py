from collections import defaultdict


def add_to_cover(cover, covered, node_with_adjacency_list):
    node, adjacency_list = node_with_adjacency_list
    cover.add(node)
    covered.add(node)
    for neighbor in adjacency_list:
        covered.add(neighbor)
    return


def to_adjacency_lists_sorted_descending_by_outdegree(edgelist):
    dictionary = defaultdict(list)
    for k, v in edgelist:
        dictionary[k].append(v)
    adjacency_lists = []
    for v in dictionary.items():
        adjacency_lists.append(v)
    adjacency_lists.sort(key=lambda tup: len(tup[1]), reverse=True)
    return adjacency_lists


def cover_greedily(edgelist):
    sorted_adjacency_lists = to_adjacency_lists_sorted_descending_by_outdegree(edgelist)

    cover = set()
    covered = set()
    for node_with_adjacency_list in sorted_adjacency_lists:
        node, adjacency_list = node_with_adjacency_list
        if not covered.__contains__(node):
            add_to_cover(cover, covered, node_with_adjacency_list)
        else:
            for neighbor in adjacency_list:
                if not covered.__contains__(neighbor):
                    add_to_cover(cover, covered, node_with_adjacency_list)
    return cover


# This is an implementation of the simple greedy algorithm for vertex cover
# Input a graph given in edge list representation
# Output a vertex cover
# The algorithm is known to be a 2-approximation

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 4), (3, 1), (3, 2), (6, 1), (8, 0), (1, 8)]
print("input graph as edge list:" + str(edges))
the_cover = cover_greedily(edges)
print("greedy cover is: " + str(the_cover))
