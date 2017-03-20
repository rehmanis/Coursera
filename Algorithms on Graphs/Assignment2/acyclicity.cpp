// file:        acyclicity.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-03
// description: Problem 1 of the second assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was : Check whether a given directed graph with n vertices 
//				and m edges contains a cycle.
//              
//				Starter file with main function was already provided but implementation of
//				DFS and acyclic functions and testing had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.01/1.00 sec, max memory used: 7.57/512 MB. 


#include <iostream>
#include <vector>

using std::vector;
using std::pair;

/**
Peforms a Depth first search on a given vertice v to check for cycles

PRE: 1 ≤ adj.size() ≤ 10e3 , 0 ≤ graph edges ≤ 10e3, visited.size() = adj.size()
POST: return true if the given vertice can reach to itself, false otherwise.
PARAM: adj = a graph in the form of adjacency list
	   visited = a vector to store the visited state of each vertice
	   u = a vertice of the graph adj 
**/
bool DFS(vector<vector<int> > &adj, vector<bool> visited, int u) {
	
	visited[u] = true;
	bool res = false;


	for (vector<int>::size_type v = 0; v < adj[u].size(); v++) {

		if (visited[adj[u][v]] == true) {
			return true;
		}

		else {

			res = DFS(adj, visited, adj[u][v]);
			if (res == true)
				return true;

		}
	}

	return false;
}

/**
Finds if there exist a cycle in the graph

PRE: 1 ≤ adj.size() ≤ 10e3 , 0 ≤ graph edges ≤ 10e3
POST: returns 1 if the graph contains a cycle , 0 otherwise
PARAM: adj = a graph in the form of adjacency list

**/

int acyclic(vector<vector<int> > &adj) {
	
	bool result;
	vector<bool> visited(adj.size(), false);

	for (vector<int>::size_type v = 0; v < adj.size(); v++) {
		

			result = DFS(adj, visited, v);
			if (result == true)
				return 1;

	}

	return 0;
}

int main() {
	
	size_t n, m;
	std::cin >> n >> m;
	vector<vector<int> > adj(n, vector<int>());
	for (size_t i = 0; i < m; i++) {
		int x, y;
		std::cin >> x >> y;
		adj[x - 1].push_back(y - 1);
	}
	std::cout << acyclic(adj);

	// Few test case to check if the acyclic function works. These are commented since the 
	// assignment requires the acyclicity.cpp file to read input values and output the respective
	// results on the console
	/********************************************************************************
	
	//Test case 1: a pair of vertices forms a cycle
	vector<vector<int> > adj1(4, vector<int>());
	adj1[1 - 1].push_back(2 - 1);
	adj1[2 - 1].push_back(1 - 1);

	if (acyclic(adj1) == 0)
		std::cout << "Test 1 failed" << std::endl;
	else
		std::cout << "Test 1 passed" << std::endl;

	//Test case 2: no cycle
	vector<vector<int> > adj2(4, vector<int>());
	adj2[1 - 1].push_back(2 - 1);
	adj2[2 - 1].push_back(3 - 1);
	adj2[3 - 1].push_back(4 - 1);

	if (acyclic(adj2) == 1)
		std::cout << "Test 2 failed" << std::endl;
	else
		std::cout << "Test 2 passed" << std::endl;

	//Test case 3: all vertice can reach from all vertices, 1 cycle
	vector<vector<int> > adj3(4, vector<int>());
	adj3[1 - 1].push_back(2 - 1);
	adj3[2 - 1].push_back(3 - 1);
	adj3[3 - 1].push_back(4 - 1);
	adj3[4 - 1].push_back(1 - 1);

	if (acyclic(adj3) == 0)
		std::cout << "Test 3 failed" << std::endl;
	else
		std::cout << "Test 3 passed" << std::endl;


	system("PAUSE");

	*************************************************************************/
}
