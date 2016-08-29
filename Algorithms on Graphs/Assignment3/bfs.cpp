// file:        bfs.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-10
// description: Problem 1 of the third assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was : Given an undirected graph with n vertices and m edges and two vertices 
//				u and v, compute the length of a shortest path between u and v(that is, the minimum 
//				number of edges in a path from u to v).
//
//				Input Format. A graph is given in the standard format. The next line contains two vertices u and v
//
//				Output: the minimum number of edges in a path from u to v, or −1 if there is no path
//              
//				Starter file with main function was already provided but implementation of
//				distance function had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.17/2.00 sec, max memory used: 40/512 MB. 

#include <iostream>
#include <vector>
#include <queue>

using std::vector;
using std::queue;
using std::pair;

// Performs breath first search to finds the length of the shortest path between
// vertice s and t of a given undirected graph adj
//
// PRE: 2 ≤ n ≤ 10e5; 0 ≤ m ≤ 10e5; t != s; 0 <= t,s < n  (note that m = edges of undirected graph
//		adj and n = size of adj)
// POST: return the shortest path between s and t if there exists one or -1 otherwise if s and t are not connected
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  s = a vertice of the graph adj
//		  t = another vertice of the graph adj (t != s)

int distance(vector<vector<int> > &adj, int s, int t) {

	//intialize an empty queue
	queue<int> myQueue;
	//intialize a vector of pairs of int and bool. Index of the vector represents the vertice number, int represents the
	//current minimum distance to reach that vertice from s and bool represent whether that vertice has been visited yet.
	vector<pair<int, bool>> dist(adj.size(), std::make_pair(0, false));
	//set the start vertice s as visited 
	dist[s].second = true;
	//push the start vertice onto the queue
	myQueue.push(s);
	//intialize a variable to keep track of the current vertice
	int w;

	//while queue is not empty
	while (!myQueue.empty())
	{
		//get the vertice from the front of the queue
		w = myQueue.front();

		//if the current vertice is the same as the target vertice, return the distance of that vertice. 
		//this is the shorted distance from s to t
		if (w == t)
			return dist[t].first;

		//remove the vertice from the front
		myQueue.pop();

		//for all vertices (adj[w][v]) reachable from w
		for (vector<int>::size_type v = 0; v < adj[w].size(); v++) {

			//if the current vertice has not yet been visited
			if (dist[adj[w][v]].second == false) {
				
				//mark it as visited
				dist[adj[w][v]].second = true;
				//push this vertice onto the queue
				myQueue.push(adj[w][v]);
				//update the distance of this vertice from w. Since all edges have same weight, we just add 1
				//to the distance at w.
				dist[adj[w][v]].first = dist[w].first + 1;
				
			}

		}
	}
	
	return -1;
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
	int s, t;
	std::cin >> s >> t;
	s--, t--;
	std::cout << distance(adj, s, t);
	
	

	// Few test case to check if the distance function works. These are commented since the 
	// assignment requires the bfs.cpp file to read input values and output the respective
	// results on the console
	/**************************************************************************************

	//Test 1
	vector<vector<int> > adj1(4, vector<int>());
	adj1[1 - 1].push_back(2 - 1);
	adj1[2 - 1].push_back(1 - 1);

	adj1[1 - 1].push_back(4 - 1);
	adj1[4 - 1].push_back(1 - 1);

	adj1[1 - 1].push_back(3 - 1);
	adj1[3 - 1].push_back(1 - 1);

	adj1[2 - 1].push_back(3 - 1);
	adj1[3 - 1].push_back(2 - 1);

	if (distance(adj1, 4 - 1, 2 - 1) == 2)
		std::cout << "Test 1 passed" << std::endl;
	else
		std::cout << "Test 1 Failed" << std::endl;

	//Test2
	if (distance(adj1, 4 - 1, 3 - 1) == 2)
		std::cout << "Test 2 passed" << std::endl;
	else
		std::cout << "Test 2 Failed" << std::endl;

	//Test 3
	vector<vector<int> > adj2(5, vector<int>());
	adj2[2 - 1].push_back(1 - 1);
	adj2[1 - 1].push_back(2 - 1);

	adj2[3 - 1].push_back(2 - 1);
	adj2[2 - 1].push_back(3 - 1);

	adj2[1 - 1].push_back(3 - 1);
	adj2[3 - 1].push_back(1 - 1);

	adj2[4 - 1].push_back(3 - 1);
	adj2[3 - 1].push_back(4 - 1);

	adj2[4 - 1].push_back(1 - 1);
	adj2[1 - 1].push_back(4 - 1);

	adj2[5 - 1].push_back(2 - 1);
	adj2[2 - 1].push_back(5 - 1);

	adj2[5 - 1].push_back(3 - 1);
	adj2[3 - 1].push_back(5 - 1);
	
	if (distance(adj2, 4 - 1, 5 - 1) == 2)
		std::cout << "Test 3 passed" << std::endl;
	else
		std::cout << "Test 3 Failed" << std::endl;

	//Test 4
	vector<vector<int> > adj3(5, vector<int>());
	adj3[5 - 1].push_back(2 - 1);
	adj3[2 - 1].push_back(5 - 1);

	adj3[1 - 1].push_back(3 - 1);
	adj3[3 - 1].push_back(1 - 1);

	adj3[3 - 1].push_back(4 - 1);
	adj3[4 - 1].push_back(1 - 1);

	adj3[1 - 1].push_back(4 - 1);
	adj3[4 - 1].push_back(1 - 1);

	if (distance(adj3, 3 - 1, 5 - 1) == -1)
		std::cout << "Test 4 passed" << std::endl;
	else
		std::cout << "Test 4 Failed" << std::endl;

	****************************************************************************************************/

	
}
