// file:        connecting_points.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-24
// description: Problem 1 of the fifth assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was: Given n points on a plane, connect them with segments of minimum total length 
//				such that there is a path between any two points.
//
//				Input Format. The first line contains the number n of points. Each of the following n lines 
//				defines a point (xi, yi).
//
//				Output: Output the minimum total length of segments. The absolute value of the difference
//				between the answer of this program and the optimal value is at most 10e−6
//
//              
//				Starter file with main function was already provided but implementation of
//				minimum_distance function had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.01/1.00 sec, max memory used: 8.7/512 MB. 


#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <queue>
#include <limits>

using std::vector;
using std::queue;
using std::pair;

// Used for creating a min priority queue i.e the top of the queue will contain
// the smallest element.

struct pri
{
	int operator() (const pair<int, double>&p1, const pair<int, double>&p2)
	{
		return (p1.second > p2.second);
	}
};

// Uses Prim's algorithm to find the optimal way to connects given points
// 
// PRE: 1 ≤ n ≤ 200; 10e-3 ≤ xi,yi ≤ 10e3 are all integers; All points (xi, yi) are pairwise different, no three
//		points lie on the same line (not xi and yi is ths same as value at x[i] and y[i], x.size() = y.size = n) 
// POST: return the minimum total length of segments (in other word the optimal way to connect all given points )
// PARAM: x = vector with all the x cordinate values of the points
//		  y = vector with all the y cordinate values of the points

double minimum_distance(vector<int> x, vector<int> y) {

	//create a min priporty queue of pairs of int and double. Int represents teh 
	std::priority_queue<int, std::vector< pair<int, double> >, pri >  min_queue;
	// create a cost vector equal to x's size and intial values of inifinity i.e a large number for all indexes 
	vector<double> cost(x.size(), std::numeric_limits<double>::max());
	cost[0] = 0.;
	//the edge weight
	double weight = 0.;
	//minimum distance i.e. lenght of the optimal way to connect given points
	double result = 0.;
	int v;
	int i = 0;
	vector<bool> visited(x.size(), false);
	
	min_queue.push(std::make_pair(0, 0));

	while (i < x.size()) {
		
		//get current index for the x and y coordinate of the point/vertice
		v = min_queue.top().first;
		//mark the index and inturn the point as visited
		visited[v] = true;
		//add the cost of the current point to the result 
		result += cost[v];
		min_queue.pop();
		
		/****
		//the whole for loop stores all the distance values from the current point to other ones in the min_queue (i.e 
		//it stores the points in increasing order of their distance from the current point)
		****/
		for (int z = 0; z < x.size(); ++z)
		{
			//if point at index z is not visited
			if (visited[z] == false) {
				//find the distance from current point at index v to point at index z and store is as the edge weight
				weight = sqrt(pow((x[v] - x[z]), 2) + pow((y[v] - y[z]), 2));
				//if the cost of reaching the next vertice from current one is greater than the edge weight,
				if (cost[z] > weight) {
					//update cost of the next vertice 
					cost[z] = weight;
					//push it on the queue
					min_queue.push(std::make_pair(z, cost[z]));
				}

			}
			//this is used to remove the duplicates pushed onto the queue i.e. prevent storing the points and their costs that have
			//already been visited 
			else if (min_queue.size() != 0) {
				while (!min_queue.empty() && visited[min_queue.top().first] == true  ) {
					min_queue.pop();
				}

			}

			
		}	
		++i;
	}
	
	return result;
}

int main() {
	
	size_t n;
	std::cin >> n;
	vector<int> x(n), y(n);
	for (size_t i = 0; i < n; i++) {
		std::cin >> x[i] >> y[i];
	}
	std::cout << std::setprecision(10) << minimum_distance(x, y) << std::endl;

	
	
	// A test case to check if the minimum_distance function works. These are commented since the 
	// assignment requires the connecting_points.cpp file to read input values and output the respective
	// results on the console
	/************************************************************************************************************
	vector<int> x1(4), y1(4);
	x1[0] = 0;
	y1[0] = 0;

	x1[1] = 0;
	y1[1] = 1;

	x1[2] = 1;
	y1[2] = 0;

	x1[3] = 1;
	y1[3] = 1;

	std::cout << std::setprecision(10) << minimum_distance(x1, y1) << std::endl;

	vector<int> x2(5), y2(5);
	x2[0] = 0;
	y2[0] = 0;

	x2[1] = 0;
	y2[1] = 2;

	x2[2] = 1;
	y2[2] = 1;

	x2[3] = 3;
	y2[3] = 0;

	x2[4] = 3;
	y2[4] = 2;

	std::cout << std::setprecision(10) << minimum_distance(x2, y2) << std::endl;

	********************************************************************************************************/
}
