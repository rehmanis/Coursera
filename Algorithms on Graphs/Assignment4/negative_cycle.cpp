// file:        negative_cycle.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-17
// description: Problem 2 of the fourth assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was: Given an directed graph with possibly negative edge weights and with n vertices and m 
//				edges, check whether it contains a cycle of negative weight.
//
//				Input Format. A graph is given in the standard format i.e on the first line input the number of nodes n
//				edges m for the graph (put a space between the two). The next lines contains two vertices u and v and 
//				the value of the edge weight from u to v. 
//
//				Output:  Output 1 if the graph contains a cycle of negative weight and 0 otherwise.
//              
//				Starter file with main function was already provided but implementation of
//				negative_cycle function had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.09/2.00 sec, max memory used: 9.9/512 MB. 

#include <iostream>
#include <vector>
#include <limits>

using std::vector;
using std::pair;

/*********************************************************************************
// We use the following lemma to check if negative weight cycle exists in the graph
//			lemma: A graph G contains a negative cycle if and only if the nth 
//				   (additional) iteration of the Bellman-Ford algorithm updates
//				   some distance values of dist vector above
***********************************************************************************/

// Uses Bellman-Ford algorithm to find whether a negative cycle exists in the graphs
// 
// PRE: 1 ≤ n ≤ 10e3; 0 ≤ m ≤ 10e4; edge weights are integers of absolute value at most 10e3
//		(note that m = edges of directed graph adj and n = size of adj)
// POST: return 1 if a negative cycle exists in the graph, 0 otherwise
// PARAM: adj = directed graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  cost = adjacency list storing edge weights of all the edges leaving each vertice


int negative_cycle(vector<vector<int> > &adj, vector<vector<int> > &cost) {

	// intialize a vector of pairs of int and bool where the first value represents the
	// current minimum distance to reach that vertice from s and second value stores a bool 
	// that represent whether that vertice has been visited yet.
	vector<pair<int, bool>> dist(adj.size(), std::make_pair(0, false));
	dist[0].second = true;
	int i = 0;
	// Used for determining if the graph has a negative cycle
	bool flag;

	
	//Run Bellman-Ford Algorithm n times (i.e adj.size() times)
	while ( i < adj.size()) {

	
		flag = false;

		for (vector<int>::size_type u = 0; u < adj.size(); u++) {
			for (vector<int>::size_type v = 0; v < adj[u].size(); v++) {
				if (dist[adj[u][v]].second == false || dist[adj[u][v]].first > dist[u].first + cost[u][v]) {

					dist[adj[u][v]].second = true;
					dist[adj[u][v]].first = dist[u].first + cost[u][v];
					flag = true;
				

				}
		
			}
		}

		//if during ith iteration of the Bellman-Ford algorithm, none of the distance values have been
		//updated, then there will also be no change to distance values during i+1 onward iterations and
		//therefore the graph does not contain a negative cycle. Return 0 in this case
		if (flag == false)
			return 0;

		++i;
	}

	//if after n iterations, the flag is still true, then it means that distance values of some nodes have
	//been updated and the graph contains negative cycle. Therefore return 1.

	return 1;
}

int main() {
	
	int n, m;
	std::cin >> n >> m;
	vector<vector<int> > adj(n, vector<int>());
	vector<vector<int> > cost(n, vector<int>());
	for (int i = 0; i < m; i++) {
		int x, y, w;
		std::cin >> x >> y >> w;
		adj[x - 1].push_back(y - 1);
		cost[x - 1].push_back(w);
	}
	std::cout << negative_cycle(adj, cost);

	// A test case to check if the negative_cycle function works. These are commented since the 
	// assignment requires the negative_cycle.cpp file to read input values and output the respective
	// results on the console
	/**************************************************************************************

	//test 1
	vector<vector<int> > adj1(4, vector<int>());
	vector<vector<int> > cost1(4, vector<int>());

	adj1[1 - 1].push_back(2 - 1);
	cost1[1 - 1].push_back(-5);

	adj1[4 - 1].push_back(1 - 1);
	cost1[4 - 1].push_back(2);

	adj1[2 - 1].push_back(3 - 1);
	cost1[2 - 1].push_back(2);

	adj1[3 - 1].push_back(1 - 1);
	cost1[3 - 1].push_back(1);

	std::cout << negative_cycle(adj1, cost1)<<std::endl; 

	***********************************************************************************************/
}
