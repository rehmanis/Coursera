"""
Functions for Prject #1: "Degree Distribution for Graphs". These functions will be
used in the Application #1: "Analysis of Citation Graphs"
"""

# define directed graph constants for testing
EX_GRAPH0 = {
    0 : set([1, 2]),
    1 : set(),
    2 : set(),
    }

EX_GRAPH1 = {
    0 : set([1, 4, 5]),
    1 : set([2, 6]),
    2 : set([3]),
    3 : set([0]),
    4 : set([1]),
    5 : set([2]),
    6 : set([]),
    }

EX_GRAPH2 = {
    0 : set([1, 4, 5]),
    1 : set([2, 6]),
    2 : set([3, 7]),
    3 : set([7]),
    4 : set([1]),
    5 : set([2]),
    6 : set(),
    7 : set([3]),
    8 : set([1, 2]),
    9 : set([0, 3, 4, 5, 6, 7]),
    }

def make_complete_graph(num_nodes):
    """
    create and return a complete graph with nodes from
    0 to num_nodes - 1 for num_nodes > 0. Otherwise
    the function returns a dictionary corresponding to
    the empty graph

    Arguments:
        num_nodes {integer} -- number of nodes for the graph

    Returns:
        dictionary -- returns a dictionary corresponding to a complete directed
        graph with the specified number of nodes.
    """
    # local variable for the complete graph
    graph = {}

    # return an empty graph if num_nodes is not positive
    if num_nodes <= 0:
        return graph

    for node in range(num_nodes):
        # create an adjacency list for a directed complete graph with no
        # self loops or parallel edges
        graph[node] = set([val for val in range(num_nodes) if val != node])

    return graph

def compute_in_degrees(digraph):
    """
    computes the in-degree of the nodes in a graph

    Arguments:
        digraph {dictionary} -- a directed graph with no self loop or parallel edges

    Returns:
        dictionary -- returns a dictionary with same set of keys(nodes) as digraph
                      whose corresponding values are the number of edges whose
                      head matches a particular node

    """

    # initialize the in degree for the nodes of digraph to 0
    in_degree = dict(zip(digraph.keys(), len(digraph) * [0]))

    for tail_node in digraph:
        for head_node in digraph[tail_node]:
            in_degree[head_node] += 1

    return in_degree

def in_degree_distribution(digraph):
    """
    computes the unnormalized distribution of the in-degrees of the graph

    Arguments:
        digraph {dictionary} -- a directed graph with no self loops or parallel
                                edges

    Returns:
        dictionary -- unnormalized distribution of the in-degrees of the graph
                      with key being the in-degree of nodes in the graph and
                      the value associated with each particular in-degree is
                      the number of nodes with that in-degree. In-degrees with
                      no corresponding nodes in the graph are not included in
                      the dictionary.
    """
    # initialize the dictionary to store
    in_degree_dist = {}
    # get the in-degree for each node
    in_degrees = compute_in_degrees(digraph)

    for degree_vals in in_degrees.values():
        if in_degree_dist.has_key(degree_vals):
            in_degree_dist[degree_vals] += 1
        else:
            in_degree_dist[degree_vals] = 1

    return in_degree_dist
