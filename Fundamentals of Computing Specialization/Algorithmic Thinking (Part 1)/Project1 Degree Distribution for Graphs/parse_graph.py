"""
Common functions used for the both Application #1 and #2
"""

def load_graph(graph_file):
    """
    Helper function to solve Q1 Application #1: Analysis of
    Citation Graphs
    converts the text representation of a graph from
    a text file to dictionary representation. 
    
    Arguments:
        graph_file {string} -- a file name of the file with text representation of a graph
    
    Returns:
        dictionary -- returns a dictionary representation of the graph
    """
    # will store the dictionary representation of the graph
    graph = {}

    with open(graph_file) as grh_file:
        for line in grh_file:
            # get the tail node and corresponding head nodes in the current
            # line of the adjacency list text representation of graph
            nodes = line.split()
            # convert the head node string to integer
            head_nodes = map(int, nodes[1:])
            # add the key, the tail node, and value, the head nodes to the
            # dictionary representation of the graph
            graph[int(nodes[0])] = set(head_nodes)
    
    return graph