// file:        shortest_path.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-17
// description: Problem 3 of the fourth assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was: Given an directed graph with possibly negative edge weights and with 
//				n vertices and m edges as well as its vertex s, compute the length of shortest paths
//				from s to all other vertices of the graph.
//
//				Input Format. A graph is given in the standard format i.e on the first line input the number of nodes n
//				edges m for the graph (put a space between the two). The next lines contains two vertices u and v and 
//				the value of the edge weight from u to v. The last line contains the vertice for which you want to find
//				the shortest path
//
//				Output:  For all vertices i from 1 to n output the following on a separate line:
//							• “*”, if there is no path from s to u;
//							• “ - ”, if there is a path from s to u, but there is no shortest path from s to u(that is, the distance
//								from s to u is −∞);
//							• the length of a shortest path otherwise
//              
//				Starter file with main function was already provided but implementation of
//				shortest_path function had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.12/2.00 sec, max memory used: 11.6/512 MB. 

#include <iostream>
#include <limits>
#include <vector>
#include <queue>

using std::vector;
using std::queue;
using std::pair;
using std::priority_queue;

// Finds the shortest path from a given vertice to every other vertice in the graph
// 
// PRE: 1 ≤ n ≤ 10e3; 0 ≤ m ≤ 10e4; edge weights are integers of absolute value at most 10e9
//		(note that m = edges of directed graph adj and n = size of adj)
// POST: updates the distance, reachable and shortest vectors that will be used in the main function
//		 to output shortest path if any
//		
// PARAM: adj = directed graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  cost = adjacency list storing edge weights of all the edges leaving each vertice
//		  s = vertice of a graph from which we want to find the shortest path to every other vertice of the graph
//		  distance = stores the minimum distance from s to all other vertices
//		  reachable = keeps track of the reachablity of all vertices from s.
//		  shortest = keeps track of the existiblity of shortest path for each vertice from s. If the shortes path 
//					 is negative infinity then, then shortes path does not exist.

void shortest_paths(vector<vector<int> > &adj, vector<vector<int> > &cost, int s, vector<long long> &distance, vector<int> &reachable, vector<int> &shortest) {

	int i = 0;
	queue<int> myQueue;
	distance[s] = 0;
	
	myQueue.push(s);
	int w;

	// run a breath first search start from s and mark all the reachable vertices from s
	while (!myQueue.empty())
	{
		w = myQueue.front();
		//stores true for all reachable vertices
		reachable[w] = 1;
		myQueue.pop();
		for (vector<int>::size_type v = 0; v < adj[w].size(); v++) {
			if (reachable[adj[w][v]]== 0) {

				myQueue.push(adj[w][v]);
				//stores true for all reachable vertices
				reachable[adj[w][v]] = 1;
			}

		}
	}


	// run Bellman-Ford algorthm n times, and store all the vertice whose distance was updated at the nth iteration in a queue
	while (i < adj.size()) {

		for (vector<int>::size_type u = 0; u < adj.size(); u++) {

			//if the distance value is infinity i.e. the vertice has not yet been visited
			if (distance[u] < std::numeric_limits<long long>::max()) {

				for (vector<int>::size_type v = 0; v < adj[u].size(); v++) {

					if (distance[adj[u][v]] == std::numeric_limits<long long>::max() || distance[adj[u][v]] > distance[u] + cost[u][v]) {

						distance[adj[u][v]] = distance[u] + cost[u][v];

						//at the nth interation, store all vertices in a queue since these are part of the negative cycle
						if (i == adj.size() - 1) {
							myQueue.push(adj[u][v]);
						}
							


					}

				}
			}

		}

		++i;
	}

	// for all vertices whose distance was updated on the nth iteration of the Bellman-Ford, mark those and all 
	// the reachable vertice from these as not having any shortest path
	while (!myQueue.empty())
	{
		w = myQueue.front();
		shortest[w] = 0;
		myQueue.pop();
		for (vector<int>::size_type v = 0; v < adj[w].size(); v++) {
			if (shortest[adj[w][v]] == 1) {
				myQueue.push(adj[w][v]);
				shortest[adj[w][v]] = 0;
			}

		}
	}



}

int main() {
	
	int n, m, s;
	std::cin >> n >> m;
	vector<vector<int> > adj(n, vector<int>());
	vector<vector<int> > cost(n, vector<int>());
	for (int i = 0; i < m; i++) {
		int x, y, w;
		std::cin >> x >> y >> w;
		adj[x - 1].push_back(y - 1);
		cost[x - 1].push_back(w);
	}
	std::cin >> s;
	s--;
	vector<long long> distance(n, std::numeric_limits<long long>::max());
	vector<int> reachable(n, 0);
	vector<int> shortest(n, 1); // 1 represents shortest path exists, 0 otherwise
	shortest_paths(adj, cost, s, distance, reachable, shortest);
	for (int i = 0; i < n; i++) {
		if (!reachable[i]) {
			std::cout << "*\n";
		}
		else if (!shortest[i]) {
			std::cout << "-\n";
		}
		else {
			std::cout << distance[i] << "\n";
		}
	}
	
	// A test case to check if the shortest_path function works. These are commented since the 
	// assignment requires the shortest_path.cpp file to read input values and output the respective
	// results on the console
	/**************************************************************************************
	
	int n = 6;
	int s = 1 - 1;
	vector<vector<int> > adj1(n, vector<int>());
	vector<vector<int> > cost1(n, vector<int>());
	vector<long long> distance1(n, std::numeric_limits<long long>::max());
	vector<int> reachable1(n, 0);
	vector<int> shortest1(n, 1); // 1 represents shortest path exists, 0 otherwise
	
	adj1[1 - 1].push_back(2 - 1);
	cost1[1 - 1].push_back(10);

	adj1[2 - 1].push_back(3 - 1);
	cost1[2 - 1].push_back(5);

	adj1[1 - 1].push_back(3 - 1);
	cost1[1 - 1].push_back(100);

	adj1[3 - 1].push_back(5 - 1);
	cost1[3 - 1].push_back(7);

	adj1[5 - 1].push_back(4 - 1);
	cost1[5 - 1].push_back(10);

	adj1[4 - 1].push_back(3 - 1);
	cost1[4 - 1].push_back(-18);
	
	adj1[6 - 1].push_back(1 - 1);
	cost1[6 - 1].push_back(-1);

	shortest_paths(adj1, cost1, s, distance1, reachable1, shortest1);
	for (int i = 0; i < n; i++) {
		if (!reachable1[i]) {
			std::cout << "*\n";
		}
		else if (!shortest1[i]) {
			std::cout << "-\n";
		}
		else {
			std::cout << distance1[i] << "\n";
		}
	}

	//test2

	n = 5;
	s = 4 - 1;
	vector<vector<int> > adj2(n, vector<int>());
	vector<vector<int> > cost2(n, vector<int>());
	vector<long long> distance2(n, std::numeric_limits<long long>::max());
	vector<int> reachable2(n, 0);
	vector<int> shortest2(n, 1); // 1 represents shortest path exists, 0 otherwise

	adj2[1 - 1].push_back(2 - 1);
	cost2[1 - 1].push_back(1);

	adj2[4 - 1].push_back(1 - 1);
	cost2[4 - 1].push_back(2);

	adj2[2 - 1].push_back(3 - 1);
	cost2[2 - 1].push_back(2);

	adj2[3 - 1].push_back(1 - 1);
	cost2[3 - 1].push_back(-5);

	std::cout << std::endl;

	shortest_paths(adj2, cost2, s, distance2, reachable2, shortest2);
	for (int i = 0; i < n; i++) {
		if (!reachable2[i]) {
			std::cout << "*\n";
		}
		else if (!shortest2[i]) {
			std::cout << "-\n";
		}
		else {
			std::cout << distance2[i] << "\n";
		}
	}


	************************************************************************************************/
}
