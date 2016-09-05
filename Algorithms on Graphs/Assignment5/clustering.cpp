// file:        clustering.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-24
// description: Problem 2 of the fifth assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was: Given n points on a plane and an integer k, compute the largest possible value 
//				of d such that the given points can be partitioned into k non - empty subsets in such a way 
//				that the distance between any two points from different subsets is at least d
//
//				Input Format. The first line contains the number n of points. Each of the following n lines 
//				defines a point (xi, yi). The last line contains the number k of clusters
//
//				Output: Output the largest value of d. The absolute value of the difference
//				between the answer of this program and the optimal value is at most 10e−6
//
//              
//				Starter file with main function was already provided
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.02/2.00 sec, max memory used: 8.6/512 MB. 

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <cmath>
#include <numeric> 

#define edge pair<int,int>

using std::vector;
using std::pair;

// sort pairs of edge and their weight based on the the weights
struct sort_pairs {
	bool operator()(const std::pair<edge, double> &left, const std::pair<edge, double> &right) {
		return left.second < right.second;
	}
};

/*
// The root, weighted_union, and find functions are for the disjoint data structure used in
// kruskal's agorithm which is implemented to solve the clustering problem.
// Source:https://www.hackerearth.com/notes/disjoint-set-union-union-find/
*/

// Return the root node of u
// 
// PRE: nodes are not forming a cycle
// POST: return the root node
// PARAM: parent = vector with indexes as nodes and their values as the node's parents
//		  u = a node for which are finding its root node
int root(vector<int> &parents, int u)
{
	//while parent of us is not u i.e u is not root
	while (parents[u] != u)
	{
		parents[u] = parents[parents[u]]; // set parent of u as it grandparent (path compression)
		u = parents[u]; 
	}
	return u;
}

// Performs a union of two different sets based on their size
// 
// PRE: root of u and root of v are not the same i.e u and v belong to different sets.
//		size of all nodes are 1 since each node makes up a set with root node being itself
// POST: updates the parent for the root node of the set with smaller size to
//		 the root of the larger set. Updates the set size accordingly
// PARAM: parent = vector with indexes as nodes and their values as the node's parents
//		  size = vector with size of each set.
//		  u = a node in a set
//		  v = a node in a different set
void weighted_union(vector<int> &parents, vector<int> &size, int u, int v) {

	int rootOfu = root(parents,u);
	int rootOfv = root(parents,v);

	//if set with node u is smaller than the set with node v
	if (size[rootOfu] < size[rootOfv]) {
		//update the parent of root node of the set with u to root node of the set with v
		parents[rootOfu] = parents[rootOfv];
		//update the size of set with v
		size[rootOfv] += size[rootOfu];
	}
	// do the oposite
	else {
		parents[rootOfv] = parents[rootOfu];
		size[rootOfu] += size[rootOfv];
	}

}

// Finds whether two nodes belong to the same set by finding their root node
// 
// PRE:  
// POST: returns true if two nodes u and v belong to the same set, false otherwise
// PARAM: parent = vector with indexes as nodes and their values as the node's parents
//		  u = a node in a set
//		  v = a node in a different set
bool find(vector<int> &parents,int u, int v)
{
	if (root(parents,u) == root(parents,v))      
		return true;
	else
		return false;
}

// Uses Kruskal's algorithm to find the the largest possible value of d such that the given points
// can be partitioned into k non - empty subsets in such a way that the distance between any two 
// points from different subsets is at least d
// 
// PRE: 2 ≤ k ≤ n ≤ 200; 10e-3 ≤ xi,yi ≤ 10e3 are all integers; All points (xi, yi) are pairwise different, 
//		(note xi and yi is ths same as value at x[i] and y[i], x.size() = y.size = n = No. of points) 
// POST: return the value d as decribed above
// PARAM: x = vector with all the x cordinate values of the points
//		  y = vector with all the y cordinate values of the points
//		  k = number of partitions to be made to the cluster of points

double clustering(vector<int> x, vector<int> y, int k) {

	//create a parent vector used for disjoint datastructure
	vector<int> parents(x.size()); 
	//update the parent vector with consecutive values from 0 to size-1
	//since initially all nodes/points are parent of itself
	std::iota(parents.begin(), parents.end(), 0); 
	//set the size of each set as 1
	vector<int> size(x.size(), 1);
	//intialize the vector of pairs of edges and their weight. Each edge contains
	//two points and the distance between them is their weight. Each point can be
	//connected to n-1 other points. Thus n point can be connected n*(n-1) points
	//which is the total number possible egde combinations
	vector < pair<edge, double> > edgeWeight(x.size()*(x.size()-1));
	edge anEdge;
	double weight;
	int v1;
	int v2;
	int counter = 0;

	/*
	//the for loop code block updated the weight of every possible edge combinations
	//between a pair of points except for the point connecting to itself (no edge to itself)
	*/
	for (int u = 0; u < x.size(); u++) {

		for (int v = 0; v < y.size(); v++) {
			if (u != v) {
				//find the distance between two points
				weight = sqrt(pow((x[u] - x[v]), 2) + pow((y[u] - y[v]), 2));
				anEdge.first = u;
				anEdge.second = v;
				edgeWeight.push_back(std::make_pair(anEdge,weight));
			}
		}
	}
	//sort egdes bases on their edge weight. Note that we will have duplicate
	//edge weights since edge from u to v will have same distance as an edge
	//from v to u
	std::sort(edgeWeight.begin(), edgeWeight.end(), sort_pairs());

	//for all possible egdes
	for (int i = 0; i < edgeWeight.size(); i++) {
		//get the points forming an egde with the next smallest weight
		v1 = edgeWeight[i].first.first;
		v2 = edgeWeight[i].first.second;
		//if these points/nodes do not belong to the same set i.e. they have different parents
		if (find(parents, v1, v2) == false) {

			//merge the two sets with v1 and v2 respectively
			weighted_union(parents, size, v1, v2);
			//update the number of edges selected for kruskal's algorithm
			++counter;
		}
		//the (n-(k-1))th edge will have the weight equal to d since this is the smallest distance
		//that connected two points in different partitions/clusters
		if (counter == (x.size() - k + 1))
			return edgeWeight[i].second;
	}

}

int main() {
	
	size_t n;
	int k;
	std::cin >> n;
	vector<int> x(n), y(n);
	for (size_t i = 0; i < n; i++) {
		std::cin >> x[i] >> y[i];
	}
	std::cin >> k;
	std::cout << std::setprecision(10) << clustering(x, y, k) << std::endl;

	// A test case to check if the clustering function works. These are commented since the 
	// assignment requires the clustering.cpp file to read input values and output the respective
	// results on the console
	/************************************************************************************************************
	
	/*
	vector<int> x1(12), y1(12);
	x1[0] = 7;
	y1[0] = 6;

	x1[1] = 4;
	y1[1] = 3;

	x1[2] = 5;
	y1[2] = 1;

	x1[3] = 1;
	y1[3] = 7;

	x1[4] = 2;
	y1[4] = 7;

	x1[5] = 5;
	y1[5] = 7;

	x1[6] = 3;
	y1[6] = 3;

	x1[7] = 7;
	y1[7] = 8;

	x1[8] = 2;
	y1[8] = 8;

	x1[9] = 4;
	y1[9] = 4;

	x1[10] = 6;
	y1[10] = 7;

	x1[11] = 2;
	y1[11] = 6;

	std::cout << std::setprecision(10) << clustering(x1, y1, 3) << std::endl;

	vector<int> x2(8), y2(8);
	x2[0] = 3;
	y2[0] = 1;

	x2[1] = 1;
	y2[1] = 2;

	x2[2] = 4;
	y2[2] = 6;

	x2[3] = 9;
	y2[3] = 8;

	x2[4] = 9;
	y2[4] = 9;

	x2[5] = 8;
	y2[5] = 9;

	x2[6] = 3;
	y2[6] = 11;

	x2[7] = 4;
	y2[7] = 12;

	std::cout << std::setprecision(10) << clustering(x2, y2, 4) << std::endl;

	*/
}
