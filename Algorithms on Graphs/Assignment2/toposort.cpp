// file:        toposort.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-03
// description: Problem 2 of the second assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was : Compute a topological ordering of a given directed 
//				acyclic graph (DAG) with n vertices and m edges 
//              
//				Starter file with main function was already provided but implementation of
//				DFS and acyclic functions and testing had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used:  0.17/2.00 sec, max memory used: 37347328/536870912 bytes. 

#include <iostream>
#include <vector>
#include <algorithm> 
//#include <ctime>

using std::vector;

// Recursively performs depth first search starting from a given vertice x and adds all the reachable
// vertices to a vector "order" starting from the sink vertice (i.e. add all vertices in post order manner)
//
// PRE: 1 ≤ adj.size() ≤ 10e5; used.size() = adj.size(), used[i] = 0 for all 0 <= i < used.size();
//		order.size() = 0 ; 0 ≤ x ≤ adj.size()-1; 
// POST: "order" contains all vertices reachable from x (including x) in post order manner.
//		 used[i] = 1 for all i = v where v = x OR/AND v = reachable vertice from x.
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and 2*m edges where n is adj.size() 
//		  used = keeps track of all the vertices that have already been visited
//		  order = used to store all the visited vertices from source vertice x in post order 
//		  x = a vertice of adj 

void dfs(vector<vector<int> > &adj, vector<int> &used, vector<int> &order, int x) {
	
	//if the vertice has not been visited and is a sink
	if (used[x] == 0 && adj[x].size() == 0) {
		used[x] = 1;			//mark as visited
		order.push_back(x);		//push it to the back of order vector
		return;					
	}
	else if (used[x] == 0) {
		used[x] = 1;			//else mark the vertice as visited

		// perfrom a depth first search on neighbour vertices reachable from x
		for (vector<int>::size_type v = 0; v < adj[x].size(); v++) {

			if (used[adj[x][v]] == 0)

				dfs(adj, used, order, adj[x][v]);
		}

		order.push_back(x);
	}


}

// Uses dfs helper function above to output the topological ordering for a given DAG adj
//
// PRE: 1 ≤ adj.size() ≤ 10e5; 
// POST: Outputs a vector with the vertices of DAG in topological ordering (i.e reverse post order) 
// PARAM: adj = an undirected acyclic graph represented in adjacancey list with n vertices and 2*m 
//		  edges where n is adj.size() 

vector<int> toposort(vector<vector<int> > adj) {

	vector<int> used(adj.size(), 0);
	vector<int> order;


	// for all vertices starting from vertice zero
	// populate the order vector containing all the visited vertices in
	// post order manner
	for (vector<int>::size_type v = 0; v < adj.size(); v++) {

		if (used[v] == 0)
			dfs(adj, used, order, v);

	}

	// reverse the order to get the topological ordering
	std::reverse(order.begin(), order.end());
	

	return order;
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
	vector<int> order = toposort(adj);
	for (size_t i = 0; i < order.size(); i++) {
		std::cout << order[i] + 1 << " ";
	}
	
	// A test case to check if the clustering function works. These are commented since the 
	// assignment requires the clustering.cpp file to read input values and output the respective
	// results on the console
	/******************************************************************************************
	//Test 1: output should be '4 3 1 2'
	vector<vector<int> > adj1(4, vector<int>());
	adj1[4 - 1].push_back(1 - 1);
	adj1[3 - 1].push_back(1 - 1);
	adj1[1 - 1].push_back(2 - 1);
	vector<int> order1 = toposort(adj1);
	for (size_t i = 0; i < order1.size(); i++) {
		std::cout << order1[i] + 1 << " ";
	}
	std::cout << std::endl;

	//Test 2: output should be '5 4 3 2 1'
	vector<vector<int> > adj2(5, vector<int>());
	adj2[4 - 1].push_back(1 - 1);
	adj2[4 - 1].push_back(3 - 1);
	adj2[3 - 1].push_back(1 - 1);
	adj2[3 - 1].push_back(2 - 1);
	adj2[5 - 1].push_back(3 - 1);
	adj2[5 - 1].push_back(2 - 1);
	adj2[2 - 1].push_back(1 - 1);
	vector<int> order2 = toposort(adj2);
	for (size_t i = 0; i < order2.size(); i++) {
		std::cout << order2[i] + 1 << " ";
	}
	std::cout << std::endl;

	vector<vector<int> > adj3(100000, vector<int>());
	vector<int> order3 = toposort(adj3);
	for (size_t i = 0; i < order3.size(); i++) {
		std::cout << order3[i] + 1 << " ";
	}
	std::cout << std::endl;

	********************************************************************************************************************/
	
}
