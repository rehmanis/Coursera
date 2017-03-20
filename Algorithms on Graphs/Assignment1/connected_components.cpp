// file:        connected_components.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-02
// description: Problem 2 of the first assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//				The task was : Given an undirected graph with n vertices and m edges, compute 
//				the number of connected component in it.
//              
//				Starter file with main function was already provided but implementation of
//				reach and number_of_components functions and testing had to be completed
//				
//				The file passed all 20 test on Coursera with
//				max time used: 0.01/1.00 sec, max memory used: 7.77/512 bytes. 

#include <iostream>
#include <vector>

using std::vector;
using std::pair;

// Recursively finds all neighbours reachable from x using depth first search 
// and updates there visited status to true
//
// PRE: 1 ≤ adj.size() ≤ 10e3; 0 ≤ x ≤ adj.size()-1; visited.size() = adj.size()
// POST: updates the visited status for all neighbours reachable from x to true 
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and 2*m edges where n is adj.size() 
//        visited = keeps track of all the vertices that have already been visited
//        x = a vertice of adj for which we want to find the reachable neighbour vertices.

void reach(vector<vector<int> > &adj, vector<bool> &visited, int x) {

	visited[x] = true;

	for (vector<int>::size_type v = 0; v < adj[x].size(); v++) {

		if (visited[adj[x][v]] == false) {

			reach(adj, visited, adj[x][v]);

		}
	}

}

// Finds the total number of connected components of the graph adj using helper function reach
// defined above.
//
// PRE: 1 ≤ adj.size() ≤ 10e3; visited.size() = adj.size();
// POST: returns the number of total connected components by finding the reachable neighbours for all vertice of adj
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and 2*m edges where n is adj.size() 
//        visited = keeps track of all the vertices that have already been visited

int number_of_components(vector<vector<int> > &adj, vector<bool> visited) {

	int res = 0;

	// iterate for all vertices of the graph
	for (vector<int>::size_type v = 0; v < adj.size(); v++) {

		if (visited[v] == false) {  // if vertice v has not yet been visited
			reach(adj, visited, v); // update all reachable vertices from v 
			++res;					// and increment the result
		}
	}

	return res;
}

int main() {

	// Few test case to check if the number_of_components function works. These are commented since the 
	// assignment requires the connected_components.cpp file to read input values and output the respective
	// results on the console
	/**************************************************************************************


	//Test 1 : graph with 8 vertices, 4 edges. 4 connected components
	vector<bool> visited1(8, false);
	vector<vector<int> > adj1(8, vector<int>());


	adj1[4 - 1].push_back(1 - 1);
	adj1[1 - 1].push_back(4 - 1);
	adj1[1 - 1].push_back(2 - 1);
	adj1[2 - 1].push_back(1 - 1);

	adj1[1 - 1].push_back(3 - 1);
	adj1[3 - 1].push_back(1 - 1);

	adj1[3 - 1].push_back(4 - 1);
	adj1[4 - 1].push_back(3 - 1);

	adj1[7 - 1].push_back(8 - 1);
	adj1[8 - 1].push_back(7 - 1);

	if (number_of_components(adj1, visited1) != 4)
		std::cout << "Test 1 failed" << std::endl;

	//Test 2 : graph with 8 vertices, 0 edges. 8 connected components
	vector<bool> visited2(8, false);
	vector<vector<int> > adj2(8, vector<int>());


	if (number_of_components(adj2, visited2) != 8)
		std::cout << "Test 2 failed" << std::endl;

	//Test 3 : graph with 8 vertices, 7 edges. 1 connected components
	vector<bool> visited3(8, false);
	vector<vector<int> > adj3(8, vector<int>());


	adj3[1 - 1].push_back(2 - 1);
	adj3[2 - 1].push_back(1 - 1);

	adj3[2 - 1].push_back(3 - 1);
	adj3[3 - 1].push_back(2 - 1);

	adj3[3 - 1].push_back(4 - 1);
	adj3[4 - 1].push_back(3 - 1);

	adj3[4 - 1].push_back(5 - 1);
	adj3[5 - 1].push_back(4 - 1);

	adj3[5 - 1].push_back(6 - 1);
	adj3[6 - 1].push_back(5 - 1);

	adj3[6 - 1].push_back(7 - 1);
	adj3[7 - 1].push_back(6 - 1);

	adj3[7 - 1].push_back(8 - 1);
	adj3[8 - 1].push_back(7 - 1);

	if (number_of_components(adj3, visited3) != 1)
		std::cout << "Test 3 failed" << std::endl;


	system("PAUSE");

	**************************************************************************************/
	// The code below was mostly provided as a part of the starter file for the assignment with few modifications

	size_t n, m;
	std::cin >> n >> m;
	vector<vector<int> > adj(n, vector<int>());
	vector<bool> visited(n, false);
	for (size_t i = 0; i < m; i++) {
		int x, y;
		std::cin >> x >> y;
		adj[x - 1].push_back(y - 1);
		adj[y - 1].push_back(x - 1);
	}
	std::cout << number_of_components(adj, visited);


}
