"""
Funtions to generate 2 types of ugraphs, the undirected ER graph
and UPA graph
"""
import random
import alg_upa_trial as upa

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


def alg_er(num_nodes, p):
    """
    generate a random graph based on Erdos Renyi(ER) model G(n, p)
    where each edge in the graph is added with probability p
    
    Arguments:
        num_nodes {integer} -- the total number of nodes for the generated graph
        p {float} -- the probability with which to add each edge to the generated graph
    
    Returns:
        dictionary -- return the ER random graph
    """

    ugraph = {}
    all_edges = []

    if (num_nodes <= 0):
        return ugraph

    # create a graph of all nodes but no edges
    for node in range(num_nodes):
        ugraph[node] = set()

    # find all possible edges of the graph
    all_edges = (set([frozenset([node1, node2]) for node1 in range(num_nodes) 
        for node2 in range(num_nodes) if node1 != node2]))
    
    # convert each edge from frozenset to list for indexing
    all_edges = [list(item) for item in all_edges]

    # add edges to the graph with probablity p
    for edge in all_edges:
        rand_prob = random.uniform(0,1)
        if rand_prob < p:
            ugraph[edge[0]].add(edge[1])
            ugraph[edge[1]].add(edge[0])

    return ugraph

def alg_upa(n_nodes, m_nodes):
    """
    Uses the DPA algorithm provided in Q3 of the Application #1
    to generates a random undirected graph iteratively, where
    each iteration a new node is created, added to the graph,
    and connected to the subset of the existing node

    Arguments:
        n_nodes {integer} -- final number of nodes in the generated graph
        m_nodes {integer} -- number of existing nodes to which a new node is connected
                             during each iteration

    Returns:
        dictionary -- the generated graph based on modified DPA algorithm for undirectef graph
    """
    # create a complete graph of m_nodes noes
    upa_graph = make_complete_graph(m_nodes)

    # create the UPAtrial object corresponding to complete graph
    upa_trial = upa.UPATrial(m_nodes)

    # add each new node to the existing graph randomly
    # chosen with probability:
    # (in-degree of new_node + 1) / (in-degree of all nodes +
    # total number of existing nodes)
    # simulated by the run_trial of the UPATrial class
    for new_node in range(m_nodes, n_nodes):
        # randomly select m_nodes from the existing graph that
        # the new_node will be connected to. Remove if any
        # duplicate nodes in the m_nodes selected
        neighbors = upa_trial.run_trial(m_nodes)

        # update the existing graph to add this new node and its
        # neighbors
        upa_graph[new_node] = neighbors

        # add this new node to all the neighbor nodes since this
        # is a undirected graph
        for neighbor in neighbors:
            upa_graph[neighbor].add(new_node)

    return upa_graph
