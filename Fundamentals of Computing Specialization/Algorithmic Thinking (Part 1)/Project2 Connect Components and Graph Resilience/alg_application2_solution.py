"""
Solutiion for Application #2: "Analysis of a Computer Network"
"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np
import alg_application2_provided as alg_app2_prov
import alg_example_graphs as alg_graphs
import alg_project2_solution as alg_proj2_sol

##### Q1 Solution #####
# To begin our analysis, we will examine the resilience of the computer network under 
# an attack in which servers are chosen at random. We will then compare the resilience 
# of the network to the resilience of ER and UPA graphs of similar size.
#
# To begin, you should determine the probability pp such that the ER graph computed 
# using this edge probability has approximately the same number of edges as the computer 
# network. (Your choice for pp should be consistent with considering each edge in the 
# undirected graph exactly once, not twice.) Likewise, you should compute an integer mm 
# such that the number of edges in the UPA graph is close to the number of edges in the 
# computer network. Remember that all three graphs being analyzed in this Application 
# should have the same number of nodes and approximately the same number of edges.

# load the graph from a text file
cnet_graph = alg_app2_prov.load_graph(alg_app2_prov.NETWORK_URL)

# get the number of nodes in the computer network graph
num_nodes = len(cnet_graph.keys())

# find the total number of edges in th computer network graph
edges = sum([len(neighbors) for  neighbors in cnet_graph.values()])/2

# find the probability such that the ER graph computed using this edge 
# probability has approximately the same number of edges as the computer network
prob_p = round(2.0 * edges / (num_nodes * (num_nodes - 1.0)), 6)

# get the average degree so that the graph created using UPA algorithm has approximately 
# same number of edges as network_graph
m_nodes = int(round(float(edges)/num_nodes))

# generate the random graph based on ER algorithm
er_graph = alg_graphs.alg_er(num_nodes, prob_p)

# generate the random graph based on UPA algorithm
upa_graph = alg_graphs.alg_upa(num_nodes, m_nodes)

# Next, you should write a function random_order that takes a graph and returns a list 
# of the nodes in the graph in some random order. Then, for each of the three graphs 
# (computer network, ER, UPA), compute a random attack order using random_order and use 
# this attack order in compute_resilience to compute the resilience of the graph.

def random_order(graph):
    """
    Take a graph a returns a random sequence of its nodes 
    Arguments:
        graph {dictionary} -- [a graph]
    
    Returns:
        list of nodes -- random sequence of nodes
    """

    lst_nodes = graph.keys()
    random.shuffle(lst_nodes)

    return lst_nodes

# compute the resilience of each of the 3 graphs
cnet_res = alg_proj2_sol.compute_resilience(cnet_graph, random_order(cnet_graph))
er_res = alg_proj2_sol.compute_resilience(er_graph, random_order(er_graph))
upa_res = alg_proj2_sol.compute_resilience(upa_graph, random_order(upa_graph))

# Once you have computed the resilience for all three graphs, plot the results as three 
# curves combined in a single standard plot (not log/log). Use a line plot for each curve. 
# The horizontal axis for your single plot be the the number of nodes removed (ranging 
# from zero to the number of nodes in the graph) while the vertical axis should be the 
# size of the largest connect component in the graphs resulting from the node removal. 
# For this question (and others) involving multiple curves in a single plot, please 
# include a legend in your plot that distinguishes the three curves. The text labels in 
# this legend should include the values for pp and mm that you used in computing the ER 
# and UPA graphs, respectively. Both matplotlib and simpleplot support these capabilities 
# (matplotlib example and simpleplot example).
# 
# Note that three graphs in this problem are large enough that using CodeSkulptor to 
# calculate compute_resilience for these graphs will take on the order of 3-5 minutes 
# per graph. When using CodeSkulptor, we suggest that you compute resilience for each 
# graph separately and save the results (or use desktop Python for this part of the 
# computation). You can then plot the result of all three calculations using simpleplot.
# load the graph from the text file

# compute the list of number of nodes removed (ranging from zero to the number of nodes in the graph)
num_removed = range(num_nodes + 1)

# plot the graphs of resilience vs number of nodes removed for each of the 3 graphs
plt.figure(0)
plt.plot(num_removed, cnet_res, '-b', label = 'computer network')
plt.plot(num_removed, er_res, '-r', label = 'ER graph p = 0.00397')
plt.plot(num_removed, upa_res, '-k', label = 'UPA graph m = 2')
plt.title('Graph resilience comparision for random attack')
plt.xlabel('number of nodes removed')
plt.ylabel('size of the largest connected component')
plt.legend(loc = 'upper right')
plt.xlim(0, None)
plt.ylim(0, 1400)
plt.grid()
# uncommet to save the plot 
#plt.savefig("Q1_graph_resilience_comparision.png")

##### Q2 Solution #####
# Consider removing a significant fraction of the nodes in each graph 
# using random_order. We will say that a graph is resilient under this 
# type of attack if the size of its largest connected component is 
# roughly (within ~25%) equal to the number of nodes remaining, after 
# the removal of each node during the attack.
#
# Examine the shape of the three curves from your plot in Question 1. 
# Which of the three graphs are resilient under random attacks as the 
# first 20% of their nodes are removed?
#
# Ans: all 3 graphs seem to be resilient, i.e the size of the largest 
# connected component is within 25% of 1000 ( the approximate number of
# remaing nodes)

##### Q3 Solution #####
# In the next three problems, we will consider attack orders in which the 
# nodes being removed are chosen based on the structure of the graph. A 
# simple rule for thesetargeted attacks is to always remove a node of 
# maximum (highest) degree from the graph. The function targeted_order(ugraph) 
# in the provided code takes an undirected graph ugraph and iteratively does 
# the following:
# 
# - Computes a node of the maximum degree in ugraph. If multiple nodes have 
#   the maximum degree, it chooses any of them (arbitrarily).
# - Removes that node (and its incident edges) from ugraph.
#
# Observe that targeted_order continuously updates ugraph and always computes 
# a node of maximum degree with respect to this updated graph. The output of 
# targeted_order is a sequence of nodes that can be used as input to compute_resilience.
# 
# As you examine the code for targeted_order, you feel that the provided 
# implementation of targeted_order is not as efficient as possible. In 
# particular, much work is being repeated during the location of nodes 
# with the maximum degree. In this question, we will consider an alternative 
# method (which we will refer to as fast_targeted_order) for computing the 
# same targeted attack order. In Python, this method creates a list 
# degree_sets whose kth element is the set of nodes of degree k. The method 
# then iterates through the list degree_sets in order of decreasing degree. 
# When it encounter a non-empty set, the nodes in this set must be of 
# maximum degree. The method then repeatedly chooses a node from this set, 
# deletes that node from the graph, and updates degree_sets appropriately.
# 
# For this question, your task is to implement fast_targeted_order and then 
# analyze the running time of these two methods on UPA graphs of size n with 
# m = 5. 

# Determine big-O bounds of the worst-case running times of targeted_order 
# and fast_targeted_order as a function of the number of nodes n in the UPA graph.
# Since the number of edges in these UPA graphs is always less than 5n (due to the 
# choice of m = 5), your big-O bounds for both functions should be expressions in n. 
# You should also assume that the all of the set operations used in fast_targeted_order 
# are O(1).
#
# Ans: target_order = O(n^2 + m) = O(n^2) since for UPA graph m <= 5n (m = total 
#      number of edges in UPA)
#      fast_target_order = O(n + m) = O(n) since for UPA graph m <= 5n (m = total
#      number of edges in UPA)

# Next, run these two functions on a sequence of UPA graphs with n in range(10,1000,10) 
# and m=5 and use the time module (or your favorite Python timing utility) to compute 
# the running times of these functions. Then, plot these running times (vertical axis) 
# as a function of the number of nodes n (horizontal axis) using a standard plot 
# (not log/log). Your plot should consist of two curves showing the results of your 
# timings. Remember to format your plot appropriately and include a legend. The title 
# of your plot should indicate the implementation of Python (desktop Python vs. CodeSkulptor) 
# used to generate the timing results.

def fast_targeted_order(graph):
    """
    Compute a targeted attack order consisting of nodes of 
    maximal degree. The algorithm used was provided.

    Arguments:
        graph {dictionary} -- a graph
    
    Returns:
        list of nodes -- a list of nodes of attack order with maximal
                         degree in descending order
    """

    # intialize the list with the target node order
    node_order = []

    # make a copy of the node
    graph_cpy = alg_app2_prov.copy_graph(graph)

    # get all the nodes of the graph
    nodes = graph_cpy.keys()

    # initialize all degree set so that all degree corresponds to empty set of nodes
    degree_set = [set() for dummy_idx in nodes]

    # add all the nodes to their corresponding degree location
    for node in nodes:
        degree = len(graph_cpy[node])
        degree_set[degree].add(node)

    # update the degree set and delete the node of the copy of graph appropriately after 
    # storing the node with current maximal degree 
    for deg_set_idx in range(len(nodes) - 1, -1, -1):
        while(len(degree_set[deg_set_idx]) != 0):
            node_u = degree_set[deg_set_idx].pop()
            for neighbor in graph_cpy[node_u]:
                degree_neigbor = len(graph_cpy[neighbor])
                degree_set[degree_neigbor].remove(neighbor)
                degree_set[degree_neigbor - 1].add(neighbor) 
            
            node_order.append(node_u)
            alg_app2_prov.delete_node(graph_cpy, node_u)


    return node_order

# intialize the fast and normal function times for targeted order
time_fast_targeted_order = []
time_targeted_order = []

# intialize the nodes to be used to generate the UPA graphs
nodes = range(10, 1000, 10)

# calcualte the time to run the normal and fast functions for the target order
for node in nodes:
    # create the UPA graph with n = node and m = 5 where m is the number of 
    # existing nodes to which a new node is connected during each iteration
    upa_graph_new = alg_graphs.alg_upa(node, 5)
    # calculate the attack order based on normal targeted order function 
    # and store the time it takes to run this function
    start = time.time()
    alg_app2_prov.targeted_order(upa_graph_new)
    end = time.time()
    time_targeted_order.append((end - start) * 1000)
    # calculate the attack order based on fast targeted order function 
    # and store the time it takes to run this function
    start = time.time()
    fast_targeted_order(upa_graph_new)
    end = time.time()
    time_fast_targeted_order.append((end - start) * 1000)

# plot the graphs of resilience vs number of nodes removed for each of the 3 graphs
plt.figure(1)
plt.plot(nodes, time_targeted_order, '-b', label = 'targeted_order')
plt.plot(nodes, time_fast_targeted_order, '-k', label = 'fast_targeted_order')
plt.title('regular vs fast runtime of targeted order in Visual Studio' )
plt.xlabel('number of nodes of UPA graph for m = 5')
plt.ylabel('run times[msec]')
plt.legend(loc = 'upper left')
plt.xlim(10, None)
plt.ylim(0, None)
plt.grid()
# uncommet to save the plot 
#plt.savefig("Q3_targeted_order_time_comparision.png")

##### Q4 Solution #####
# To continue our analysis of the computer network, we will examine its resilience 
# under an attack in which servers are chosen based on their connectivity. We will 
# again compare the resilience of the network to the resilience of ER and UPA graphs 
# of similar size.
# 
# Using targeted_order (or fast_targeted_order), your task is to compute a targeted 
# attack order for each of the three graphs (computer network, ER, UPA) from Question 1. 
# Then, for each of these three graphs, compute the resilience of the graph using 
# compute_resilience. Finally, plot the computed resiliences as three curves (line plots) 
# in a single standard plot. As in Question 1, please include a legend in your plot that 
# distinguishes the three plots. The text labels in this legend should include the values 
# for p and m that you used in computing the ER and UPA graphs, respectively.

# compute the target order for the 3 graph in Q1
tar_order_cnet = fast_targeted_order(cnet_graph)
tar_order_er = fast_targeted_order(er_graph)
tar_order_upa = fast_targeted_order(upa_graph)

# compute the resilience for the 3 graph using the targeted order
# compute the resilience of each of the 3 graphs
cnet_res = alg_proj2_sol.compute_resilience(cnet_graph, tar_order_cnet)
er_res = alg_proj2_sol.compute_resilience(er_graph, tar_order_er)
upa_res = alg_proj2_sol.compute_resilience(upa_graph, tar_order_upa)

# plot the computer resilience for the targeted order for the 3 graph
plt.figure(2)
plt.plot(num_removed, cnet_res, '-b', label = 'computer network')
plt.plot(num_removed, er_res, '-r', label = 'ER graph p = 0.00397')
plt.plot(num_removed, upa_res, '-k', label = 'UPA graph m = 2')
plt.title('Graph resilience comparision for targeted order')
plt.xlabel('number of nodes removed')
plt.ylabel('size of the largest connected component')
plt.legend(loc = 'upper right')
plt.xlim(0, None)
plt.ylim(0, 1400)
plt.grid()
plt.show()
# uncommet to save the plot 
#plt.savefig("Q4_graph_resilience_comparision.png")

##### Q5 Solution #####
# Examine the shape of the three curves from your plot in Question 4. 
# Which of the three graphs are resilient under targeted attacks as 
# the first 20% of their nodes are removed? Again, note that there is 
# no need to compare the three curves against each other in your answer 
# to this question.
#
# Ans: From the graph we can see that only ER graph is resilient as the 
# first 20% of the nodes are removed while the UPA and the computer
# network graph reaches close to zero as 20% of the ndoes are removed
