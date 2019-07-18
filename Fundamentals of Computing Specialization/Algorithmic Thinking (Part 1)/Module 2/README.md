# Project and Application Overviews
## Project #2: Connect Components and Graph Resilience 

* For the Project component of Module 2, you will first write Python code that implements breadth-first search. Then, you will use this function to compute the set of connected components (CCs) of an undirected graph as well as determine the size of its largest connected component. Finally, you will write a function that computes the resilience of a graph (measured by the size of its largest connected component) as a sequence of nodes are deleted from the graph.

* You will use these functions in the Application component of Module 2 where you will analyze the resilience of a computer network, modeled by a graph. As in Module 1, graphs will be represented using dictionaries.

Complete project description can be found at : 
<https://www.coursera.org/learn/algorithmic-thinking-1/supplement/9tlQe/project-2-description>

## Application #2: Analysis of a Computer Network

* Graph exploration (that is, "visiting" the nodes and edges of a graph) is a powerful and necessary tool to elucidate properties of graphs and quantify statistics on them. For example, by exploring a graph, we can compute its degree distribution, pairwise distances among nodes, its connected components, and centrality measures of its nodes and edges. As we saw in the Homework and Project, breadth-first search can be used to compute the connected components of a graph.

* In this Application, we will analyze the connectivity of a computer network as it undergoes a cyber-attack. In particular,we will simulate an attack on this network in which an increasing number of servers are disabled. In computational terms, we will model the network by an undirected graph and repeatedly delete nodes from this graph. We will then measure the resilience of the graph in terms of the size of the largest remaining connected component as a function of the number of nodes deleted.

Complete application description can be found at : 
<https://www.coursera.org/learn/algorithmic-thinking-1/supplement/0ekiq/application-2-description>