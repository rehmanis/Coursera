// file:        dijkstra.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-17
// description: Problem 1 of the fourth assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was: Given an directed graph with positive edge weights and with n vertices and m edges as well as two
//				vertices u and v, compute the weight of a shortest path between u and v(that is, the minimum total
//				weight of a path from u to v).
//
//				Input Format. A graph is given in the standard format i.e on the first line input the number of nodes n
//				edges m for the graph (put a space between the two). The next lines contains two vertices u and v and 
//				the value of the edge weight from u to v. The last line contains the vertice u and v for which we want to 
//				find the minimum distance from u to v.  
//
//				Output:  Output the minimum weight of a path from u to v, or −1 if there is no path
//
//              
//				Starter file with main function was already provided but implementation of
//				distance function had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.14/2.00 sec, max memory used: 41.4/512 MB. 

#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using std::vector;
using std::queue;
using std::pair;

// Used for creating a min priority queue i.e the top of the queue will contain
// the smallest element.
struct pri
{
	int operator() (const pair<int, int>&p1, const pair<int, int>&p2)
	{
		return (p1.second > p2.second);
	}
};

// Performs breath first search to finds the minimum weight of the path from s to t or returns -1
// if no path exists
// 
// PRE: 1 ≤ n ≤ 10e3; 0 ≤ m ≤ 10e5; t != s; 0 <= t,s < n; edge weights are non-negative integers not
// exceeding 10e3 (note that m = edges of undirected graph adj and n = size of adj)
// POST: return the shortest path between s and t if there exists one or -1 otherwise if s and t are not connected
// PARAM: adj = undirected graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  cost = adjacency list storing edge weights of all the edges leaving each vertice
//		  s = a vertice of the graph adj
//		  t = another vertice of the graph adj (t != s)

int distance(vector<vector<int> > &adj, vector<vector<int> > &cost, int s, int t) {

	// intialize a min priority queue that stores a vector of pairs with first value of
	// the pair being the vertice number while second being the current minimum distance
	// to reach that vertice
	std::priority_queue<int, std::vector< pair<int,int> >, pri >  min_queue;
	// intialize a vector of pairs of int and bool where the first value represents the
	// current minimum distance to reach that vertice from s and second value stores a bool 
	// that represent whether that vertice has been visited yet.
	vector<pair<int, bool>> dist(adj.size(), std::make_pair(0, false));
	//set the start vertice s as visited 
	dist[s].second = true;

	//push the start vertice onto the queue
	min_queue.push(std::make_pair(s, dist[s].first));
	//intialize a variable to keep track of the current vertice
	int w;


	while (!min_queue.empty())
	{
		w = min_queue.top().first;
		//if the current vertice is the same as the target vertice, return the distance of that vertice. 
		//this is the shorted distance from s to t
		if (w == t)
			return dist[t].first;
		min_queue.pop();

		//for all vertices reachable from w
		for (vector<int>::size_type v = 0; v < adj[w].size(); v++) {

			// if the current vertice has not yet been visited or the current minimum distance of that vertice 
			// (s to the vertice) is greater than the distance at w + distance from w to that vertice
			if (dist[adj[w][v]].second == false || dist[adj[w][v]].first > dist[w].first + cost[w][v]) {

				//mark it as visited
				dist[adj[w][v]].second = true;
				//update the distance of this vertice from w. 
				dist[adj[w][v]].first = dist[w].first + cost[w][v];
				min_queue.push(std::make_pair(adj[w][v], dist[adj[w][v]].first));
				
			}
		}
	}

	return -1;
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
	int s, t;
	std::cin >> s >> t;
	s--, t--;
	std::cout << distance(adj, cost, s, t);

	// Few test case to check if the distance function works. These are commented since the 
	// assignment requires the bfs.cpp file to read input values and output the respective
	// results on the console
	/**************************************************************************************
	
	/*
	//test 1
	vector<vector<int> > adj1(4, vector<int>());
	vector<vector<int> > cost1(4, vector<int>());

	adj1[1 - 1].push_back(2 - 1);
	cost1[1 - 1].push_back(1);

	adj1[4 - 1].push_back(1 - 1);
	cost1[4 - 1].push_back(2);

	adj1[2 - 1].push_back(3 - 1);
	cost1[2 - 1].push_back(2);

	adj1[1 - 1].push_back(3 - 1);
	cost1[1 - 1].push_back(5);

	std::cout << distance(adj1, cost1, 1-1, 3-1) << std::endl;

	//test 2
	vector<vector<int> > adj2(5, vector<int>());
	vector<vector<int> > cost2(5, vector<int>());

	adj2[1 - 1].push_back(2 - 1);
	cost2[1 - 1].push_back(4);

	adj2[1 - 1].push_back(3 - 1);
	cost2[1 - 1].push_back(2);

	adj2[2 - 1].push_back(3 - 1);
	cost2[2 - 1].push_back(2);

	adj2[3 - 1].push_back(2 - 1);
	cost2[3 - 1].push_back(1);

	adj2[2 - 1].push_back(4 - 1);
	cost2[2 - 1].push_back(2);

	adj2[3 - 1].push_back(5 - 1);
	cost2[3 - 1].push_back(4);

	adj2[5 - 1].push_back(4 - 1);
	cost2[5 - 1].push_back(1);

	adj2[2 - 1].push_back(5 - 1);
	cost2[2 - 1].push_back(3);

	adj2[3 - 1].push_back(4 - 1);
	cost2[3 - 1].push_back(4);

	std::cout << distance(adj2, cost2, 1 - 1, 5 - 1) << std::endl;

	//test 3
	vector<vector<int> > adj3(3, vector<int>());
	vector<vector<int> > cost3(3, vector<int>());

	adj3[1 - 1].push_back(2 - 1);
	cost3[1 - 1].push_back(7);

	adj3[1 - 1].push_back(3 - 1);
	cost3[1 - 1].push_back(5);

	adj3[2 - 1].push_back(3 - 1);
	cost3[2 - 1].push_back(2);

	std::cout << distance(adj3, cost3, 3 - 1, 2 - 1) << std::endl;

	system("PAUSE");
	*/
}
