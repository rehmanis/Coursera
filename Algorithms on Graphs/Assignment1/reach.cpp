// file:        reach.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-01
// description: Problem 1 of the first assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was : Given an undirected graph and two distinct vertices u and v, 
//				check if there is a path between u and v
//              
//				Starter file with main function was already provided but implementation of
//				reach function and testing had to be completed
//				
//				The file passed all 20 test on Coursera with
//				max time used: 0.01/1.00 sec, max memory used: 7.73/512 MB. 

#include <iostream>
#include <vector>

using std::vector;

// Recursively computes whether a path exists between x and y using depth first search
//
// PRE: 1 ≤ adj.size() ≤ 10e3; 0 ≤ x, y ≤ adj.size()-1; x != y
// POST: returns 1 for path between x and y, 0 otherwise
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and 2*m edges where n is adj.size() 
//		  visited = keeps track of all the vertices that have already been visited
//		  x = one of the vertice of adj
//		  y = another vertice of adj not equal to x

int reach(vector<vector<int> > &adj, vector<bool> visited, int x, int y) {

	int value = 0;

	visited[x] = true; // mark the first vertice as true

	// iterate for all edges of x
	for (vector<int>::size_type v = 0; v < adj[x].size(); v++) {

		if (visited[adj[x][v]] == false) {
			if (adj[x][v] == y) // if the target vertice y is connected to the edge from x, return 1
				return 1;
			
			else {
				value = reach(adj, visited, adj[x][v], y); // perform a depth first search with new x value
				if (value == 1) // if x = y during the depth first search, return 1.
					return 1;
			}
		}
	}


	return value;
}

int main() {
	
	// Few test case to check if the reach function works. These are commented since the 
	// assignment requires the reach.cpp file to read input values and output the respective
	// results on the console
	/**************************************************************************************

	int n = 8;
	vector<bool> visited(n, false);
	vector<vector<int> > adj(n, vector<int>());


	adj[4 - 1].push_back(1 - 1);
	adj[1 - 1].push_back(4 - 1);
	adj[1 - 1].push_back(2 - 1);
	adj[2 - 1].push_back(1 - 1);

	adj[1 - 1].push_back(3 - 1);
	adj[3 - 1].push_back(1 - 1);

	adj[3 - 1].push_back(4 - 1);
	adj[4 - 1].push_back(3 - 1);

	adj[7 - 1].push_back(8 - 1);
	adj[8 - 1].push_back(7 - 1);

	//test Case 1: No neighbours in adjacency list for both nodes
	if (reach(adj, visited, 5-1, 6-1 ) != 0) {
	std::cout << "Test case 1 failed" << std::endl;
	}

	//test Case 2: No egde between the two nodes but the nodes have some neighbours
	if (reach(adj, visited, 7 - 1, 2 - 1) != 0) {
	std::cout << "Test case 2 failed" << std::endl;
	}

	//test Case 3: a direct edge connecting the two nodes
	if (reach(adj, visited, 3 - 1, 1 - 1) != 1) {
	std::cout << "Test case 3 failed" << std::endl;
	}

	//test Case 4: an indirect path connecting the two nodes
	if (reach(adj, visited, 4 - 1, 2 - 1) != 1) {
	std::cout << "Test case 4 failed" << std::endl;
	}

	system("PAUSE");
	
	**************************************************************************************/
	// The code below was mostly provided as a part of the starter file for the assignment with few modifications

	size_t n, m;
	std::cin >> n >> m;
	vector<bool> visited(n, false);
	vector<vector<int> > adj(n, vector<int>());
	for (size_t i = 0; i < m; i++) {
		int x, y;
		std::cin >> x >> y;
		adj[x - 1].push_back(y - 1);
		adj[y - 1].push_back(x - 1);
	}
	int x, y;
	std::cin >> x >> y;
	std::cout << reach(adj, visited, x - 1, y - 1) << std::endl;
	
	
}













