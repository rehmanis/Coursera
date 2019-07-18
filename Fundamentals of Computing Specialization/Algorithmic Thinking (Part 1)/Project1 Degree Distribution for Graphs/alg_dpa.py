"""
Algorithm to generate DPA graph 
"""
import deg_dis_for_graphs as deg_funcs
import alg_dpa_trial as dpa

def alg_dpa(n_nodes, m_nodes):
    """
    Uses the DPA algorithm provided in Q3 of the Application
    to generates a random directed graph iteratively, where
    each iteration a new node is created, added to the graph,
    and connected to the subset of the existing node

    Arguments:
        n_nodes {integer} -- final number of nodes in the generated graph
        m_nodes {integer} -- number of existing nodes to which a new node is connected
                            during each iteration

    Returns:
        dictionary -- the generated graph based on DPA algorithm
    """

    # create a complete graph of m_nodes noes
    dpa_graph = deg_funcs.make_complete_graph(m_nodes)

    # create the DPA trial object corresponding to complete graph
    dpa_trial = dpa.DPATrial(m_nodes)

    # add each new ode to m_nodes from the existing graph randomly
    # chosen with probability:
    # (in-degree of new_node + 1) / (in-degree of all nodes +
    # total number of existing nodes)
    # simulated by the run_trial of the DPATrial class
    for new_node in range(m_nodes, n_nodes):
        # randomly select m_nodes from the existing graph that
        # the new_node will be connected to. Remove if any
        # duplicate nodes in the m_nodes selected
        neighbors = dpa_trial.run_trial(m_nodes)

        # update the existing graph to add this new node and its
        # neighbors
        dpa_graph[new_node] = neighbors


    return dpa_graph
