"""
Functions for Project #2: "Connected Components and Graph Resilience". These 
functions will be used for the Application #2: "Analysis of a Computer Network"
"""
from collections import deque
import alg_application2_provided as alg_app2_prov

def bfs_visited(ugraph, start_node):
    """
    Perfoms the Breath First Seach(BFS) and returns a set of all the nodes 
    that are visited starting from start_node
    
    Arguments:
        ugraph {dictionary} -- an undirect graph
        start_node {integer} -- a node in the ugraph
    
    Returns:
        set -- a set of all nodes visited by a BFS that start at start_node
    """
    # initialize an queue with the start_node. We use python's built in double
    # ended queue, deque
    deq = deque([start_node])
    # add the start node to the visited nodes set
    visited = set([start_node]) 
    # keep traversing through all the neighbors of the nodes in the queue
    # as long as the queue is not empty and mark them as visited if the nodes
    # are not yet visited
    while len(deq) != 0:
        curr_node = deq.popleft()
        for neighbor in ugraph[curr_node]:
            if not (neighbor in visited):
                visited.add(neighbor)
                deq.append(neighbor)

    return visited

def cc_visited(ugraph):
    """
    Takes an undirected graph ugraph and computes the all the
    connected components of the graph
    
    Arguments:
        ugraph {dictionary} -- an undirected graph
    
    Returns:
        list of sets -- resturns a list of sets where each set has all the nodes in
                        a particular connected component of the graph, and each set
                        represent a connect component of the graph
    """
    # initialize the remaining nodes in the ugraph that have not yet been visited 
    remain_nodes = set(ugraph.keys())
    # initiakize the list of sets where each set is a connected component of ugraph
    con_comp = []

    # use BFS to find all the connect components until all the nodes of the ugraph
    # have been visisted
    while len(remain_nodes) != 0:
        not_vis_node = remain_nodes.pop()
        visited = bfs_visited(ugraph, not_vis_node)
        con_comp.append(visited)
        remain_nodes -= visited

    return con_comp

def largest_cc_size(ugraph):
    """
    Takes a undirected graph and returns the size of the largest connected component
    
    Arguments:
        ugraph {dictionary} -- an undirected graph
    
    Returns:
        integer -- the size of the largest connected component of ugraph
    """
    # find the size of all the connect components of the ugraph
    len_cc = [len(con_comp) for con_comp in cc_visited(ugraph)]
    
    # make sure to take care of the case when ugraph is empty and we get
    # an empty len_cc list
    if (len(len_cc) == 0):
        return 0

    # return the max size of connected compo
    return max(len_cc)

def compute_resilience(ugraph, attack_order):
    """
    Computes a measure of resilience of an undirected graph. Takes the undirected 
    graph ugraph, a list of nodes attack_order and iterates through the nodes in 
    attack_order. For each node in the list, the function removes the given node 
    and its edges from the graph and then computes the size of the largest connected 
    component for the resulting graph.
    
    Arguments:
        ugraph {dictionary} -- an undirected graph
        attack_order {list of nodes} -- list of nodes that will be iterated over
    
    Returns:
        list of integers -- return a list whose (k+1)th entry is the size of the largest 
                            connected component in the graph after the removal of the first 
                            k nodes in attack_order
    """
    new_graph = alg_app2_prov.copy_graph(ugraph)

    # get the size of the largest connected component before removing any nodes
    lst_max_cc = [largest_cc_size(new_graph)]

    # start removing each node in the attack_order and its edges from the ugraph
    # and find the largest connected component after each removal 
    for remove_node in attack_order:
        alg_app2_prov.delete_node(new_graph, remove_node)
        lst_max_cc.append(largest_cc_size(new_graph))

    return lst_max_cc
