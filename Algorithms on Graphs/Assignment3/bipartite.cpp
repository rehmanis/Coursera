// file:        bipartite.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-10
// description: Problem 2 of the third assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was : Given an undirected graph with n vertices and m edges, check whether it is bipartite.
//
//				Input Format. A graph is given in the standard format i.e on the first line input the number of nodes n
//				and edges m for the graph (put a space between the two). 
//
//				Output:  Output 1 if the graph is bipartite and 0 otherwise.
//
//              
//				Starter file with main function was already provided but implementation of
//				bipartite function had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.17/2.00 sec, max memory used: 41.9/513 MB. 


#include <iostream>
#include <vector>
#include <queue>

using std::vector;
using std::queue;

// Finds whether the given graph is bipartite. See http://mathworld.wolfram.com/BipartiteGraph.html
// for details on bipartite graph
//
// PRE: 1 ≤ n ≤ 10e5; 0 ≤ m ≤ 10e5; t != s; 0 < t,s < n -1 (note that m = edges of undirected graph
//		adj and n = size of adj)
// POST: return 1 if the graph adj is bipartite or 0 otherwise
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and 2*m edges where n is adj.size() 

int bipartite(vector<vector<int> > &adj) {

	queue<int> myQueue;

	//white color (first color) is represented by 1, black (second color) by 0 and nodes
	//that are not yet colored are represented by -1
	vector<int> colors(adj.size(), -1);

	myQueue.push(0);
	//colors source node white
	colors[0] = 1;

	int u;

	//run BFS while queue is not empty
	while (!myQueue.empty())
	{
		//store the node at front and dequeue it
		u = myQueue.front();
		myQueue.pop();

		//explore all nodes adjacent to u
		for (vector<int>::size_type v = 0; v < adj[u].size(); v++) {

			//if the node adjacent to u is not colored
			if (colors[adj[u][v]] == -1) {

				//assign an alternate colors.
				colors[adj[u][v]] = 1 - colors[u];
				myQueue.push(adj[u][v]);
			}
			//else if the adjacent node is the same color as u, then the graph cannot be bipartite
			else if (colors[adj[u][v]] == colors[u])
				return 0;

		}
	}

	return 1;
}

int main() {
	
	int n, m;
	std::cin >> n >> m;
	vector<vector<int> > adj(n, vector<int>());
	for (int i = 0; i < m; i++) {
		int x, y;
		std::cin >> x >> y;
		adj[x - 1].push_back(y - 1);
		adj[y - 1].push_back(x - 1);
	}
	std::cout << bipartite(adj);
	

	// Few test case to check if the bipartite function works. These are commented since the 
	// assignment requires the bipartite.cpp file to read input values and output the respective
	// results on the console
	/******************************************************************************************
	//Test 1
	vector<vector<int> > adj1(4, vector<int>());
	adj1[1 - 1].push_back(2 - 1);
	adj1[2 - 1].push_back(1 - 1);

	adj1[4 - 1].push_back(1 - 1);
	adj1[1 - 1].push_back(4 - 1);

	adj1[2 - 1].push_back(3 - 1);
	adj1[3 - 1].push_back(2 - 1);

	adj1[3 - 1].push_back(1 - 1);
	adj1[1 - 1].push_back(3 - 1);

	if (bipartite(adj1) == 0)
		std::cout << "Test 1 passed" << std::endl;
	else
		std::cout << "Test 1 failed" << std::endl;

	//test2
	vector<vector<int> > adj2(5, vector<int>());
	adj2[5 - 1].push_back(2 - 1);
	adj2[2 - 1].push_back(5 - 1);

	adj2[4 - 1].push_back(2 - 1);
	adj2[2 - 1].push_back(4 - 1);

	adj2[3 - 1].push_back(4 - 1);
	adj2[4 - 1].push_back(3 - 1);

	adj2[1 - 1].push_back(4 - 1);
	adj2[4 - 1].push_back(1 - 1);

	if (bipartite(adj2) == 1)
		std::cout << "Test 2 passed" << std::endl;
	else
		std::cout << "Test 2 failed" << std::endl;

	system("PAUSE");
	*******************************************************************************************************/

}
