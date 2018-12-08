from collections import defaultdict


def add_to_cover(cover, covered, node_with_adjacency_list):
    node, adjacency_list = node_with_adjacency_list
    cover.add(node)
    covered.add(node)
    for neighbor in adjacency_list:
        covered.add(neighbor)
    return


def to_adjacency_lists_sorted_descending_by_degree(edge_list):
    dictionary = defaultdict(list)
    for k, v in edge_list:
        dictionary[k].append(v)
    adjacency_lists = []
    for v in dictionary.items():
        adjacency_lists.append(v)
    adjacency_lists.sort(key=lambda tup: len(tup[1]), reverse=True)
    return adjacency_lists


def cover_uncovered_edges(edge_list, cover):
    for edge in edge_list:
        (u, v) = edge
        if not cover.__contains__(u) and not cover.__contains__(v):
            cover.add(u)
    return cover


# This is an implementation of the simple greedy algorithm for vertex cover
# Input a graph given in edge list representation
# Output a vertex cover
# The algorithm is known to be a 2-approximation
def cover_greedily(graph):
    # greedy means here: select vertices with high degree first
    sorted_adjacency_lists = to_adjacency_lists_sorted_descending_by_degree(graph.edge_list())

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
    return cover_uncovered_edges(graph.edge_list(), cover)
