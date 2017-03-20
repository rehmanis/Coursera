// file:        strongly_connected.cpp
// author:      Shamsuddin Rehmani
// date:        2016-07-31
// description: Problem 3 of the second assignment of Algorithms on Graphs
//				by University of California, San Diego & Higher School of Economics on Coursera
//
//              The task was : Compute the number of strongly connected components of a given
//				directed graph with n vertices and m edges.
//              
//				Starter file with main function was already provided but implementation of
//				all other functions had to be completed
//				
//				The file passed all test cases on Coursera with
//				max time used: 0.09/1.00 sec, max memory used: 11.02/512 MB. 


#include <algorithm>
#include <iostream>
#include <vector>
#include <numeric>


// first element stores number for each node visited in pre-order while the second one
// stores post order visit number for that node
#define preAndPost pair<int,int>

using std::vector;
using std::pair;

//sort criteria based on max post order number
struct sort_pairs {
	bool operator()(const std::pair<preAndPost, int> &left, const std::pair<preAndPost, int> &right) {
		return left.first.second > right.first.second;
	}
};

// Takes a Directed Graph and reverses its edges
//
// PRE: 1 ≤ adj.size() ≤ 10e4; number of edges of adj is between 0 and 10e4; rev_adj.size() = adj.size()
//		number of edges of rev_adj is 0.
//
// POST: updates rev_adj such that all the edges of adj are reversed.
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  rev_adj = a graph with only nodes but no edges
void reverse_graph(vector< vector <int> > adj, vector< vector <int> > &rev_adj) {



	for (vector<int>::size_type v = 0; v < adj.size(); v++) {
		for (vector<int>::size_type u = 0; u < adj[v].size(); u++) {
			rev_adj[adj[v][u]].push_back(v);
		}
	}

}

// Recursively updates the visited status of all the nodes of the graph adj
//
// PRE: 1 ≤ adj.size() ≤ 10e4; number of edges of adj is between 0 and 10e4; visited.size() = adj.size()	
//
// POST: updates visited vector with 1 for nodes visited and sends the total number of nodes that were visited.
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  visited = keeps track of all the vertices that have already been visited
//		  x = the vertice and its reachable neighbours to be marked visited
//		  i = a variable used to keep track of total number of visited nodes in each function call.

int mark_visited(vector<vector<int> > &adj, vector<int> &visited, int x, int i) {

	if (adj[x].size() == 0) {

		visited[x] = 1;
		return 1;
	}

	visited[x] = 1;
	i++;

	for (vector<int>::size_type v = 0; v < adj[x].size(); v++) {

		if (visited[adj[x][v]] == 0) {

			i = mark_visited(adj, visited, adj[x][v], i);

		}
	}

	return i;
}


// Recursively updates the pre_pos vector with pre and post order visit number of a vertice and it reachable 
// neighbours. Returns the largest post order visit number. 
//
// PRE: 1 ≤ adj.size() ≤ 10e4; number of edges of adj is between 0 and 10e4; visited.size() = adj.size();
//		pre_pos.size() = adj.size(). 0 <= x < adj.size(). 0 <= i < adj.size()*2
//
// POST: updates visited vector with 1 for nodes visited and pre_pos vector with pre and post visit numbers
//		 and their respective vertices. Returns the maximum post order visit number from visited nodes
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  visited = keeps track of all the vertices that have already been visited
//		  pre_pos = stores the vertice and it respective pre and post order visit number.
//		  x = the vertice and its reachable neighbours to be marked visited and their pre and post order numbers
//			  to updated accordingly.
//		  i = Used to keep track of the pre and post order visit numbers

int explore(vector<vector<int> > &adj, vector<int> &visited, vector< pair <preAndPost, int > > &pre_pos, int x, int i) {


	if (adj[x].size() == 0) {

		pre_pos[x].first.first = i;
		pre_pos[x].first.second = i + 1;
		pre_pos[x].second = x;
		visited[x] = 1;
		return i + 1;

	}
	//mark the current node (i.e. x as visited)
	visited[x] = 1;

	//update the pre order visit number
	pre_pos[x].first.first = i;
	//associate this pre order number with the current vertice x
	pre_pos[x].second = x;

	for (vector<int>::size_type v = 0; v < adj[x].size(); v++) {

		if (visited[adj[x][v]] == 0) {

			// Do Depth first exploration of neighbours of the current vertice x and mark
			// their pre and post order visit numbers recursively
			i = explore(adj, visited, pre_pos, adj[x][v], i + 1);

		}
	}

	//update the post order number
	pre_pos[x].first.second = i + 1;

	return i + 1;


}

// Updates the pre_pos vector with pre and post order visit number of all vertices in a graphs using the helper
// function explore
//
// PRE: 1 ≤ adj.size() ≤ 10e4; number of edges of adj is between 0 and 10e4; visited.size() = adj.size();
//		pre_pos.size() = adj.size(). 
// POST: updates pre_pos vector with pre and post visit numbers for the given graph adj
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and m edges where n is adj.size() 
//		  visited = keeps track of all the vertices that have already been visited
//		  pre_pos = stores the vertice and it respective pre and post order visit number.

void DFS(vector< vector <int> > adj, vector<int> visited, vector< pair< preAndPost, int > > &pre_pos) {

	int i = 0;

	for (vector<int>::size_type v = 0; v < adj.size(); v++) {

		if (visited[v] == 0) {

			
			i = explore(adj, visited, pre_pos, v, i);
			
			i++;
		}
	}


}


//The idea behind finding the strongly connected components is as follows:
/***************************************************************************************************************************
// if v is in the sink strongly connected component (SSC)--v may not be a sink itself--then
// all the vertice reachable from v and v itself form a SSC. Thus if we find a vertice in sink SCC
// and explore all the vertice reachable from it, we can find one strongly connected component of a graph
//
// In order to do so we use the following theorem:
// --- "If C and C' are two SSC where there's an edge from some vertex of C to some vertex of C'.
//	   The largest post number in C Is larger than the largest post number in C'." ---taken from
//	   the lecture slides for this coure
//
// However, the largest post number is in the source SSC. Thus we reverse the given graph find the source SSC, which
// is the sink SSC of the original graph by marking the pre and post number using the explore function above. The vertice
// with the highest post number and all the reachable vertice from it forms a SSC. Next we explore the vertice with the second
// largest post number and find all the reachable vertices from it to get the next SSC. We continue doing this until we have
// visited all the vertices.
//
***************************************************************************************************************************/

// Finds the number of strongly connected components of the graph
// function explore
//
// PRE: 1 ≤ adj.size() ≤ 10e4; number of edges of adj is between 0 and 10e4;  
// POST: returns the total number of strongly connected component of the graph adj
// PARAM: adj = an undirected graph represented in adjacancey list with n vertices and m edges where n is adj.size() 

int number_of_strongly_connected_components(vector< vector<int> > adj) {


	//To keep track of the total number of strongly connected components
	int result = 0;
	//Used to get the vertice with highest post order visit number
	int maxPosVer = 0;
	int adjSize = adj.size();
	int i = 0;

	vector< int > visited(adj.size(), 0);
	vector<vector <int> > rev_adj(adj.size(), vector<int>());
	vector< pair <preAndPost, int > > pre_pos(adj.size());

	
	//reverse the edges of the given graph
	reverse_graph(adj, rev_adj);

	//mark pre and post number on the vertice of this reverse graph
	DFS(rev_adj, visited, pre_pos);

	//sort based on the vertice with highest post number to the lowest one
	std::sort(pre_pos.begin(), pre_pos.end(), sort_pairs());

	//while all the vertices have not be visited
	while (i < adjSize) {

		for (vector<int>::size_type v = 0; v < adj.size(); v++) {
			//if the vertice has not been visited
			if (visited[pre_pos[v].second] == 0) {

				//store the vertice with the highest post number
				maxPosVer = pre_pos[v].second;
				break;
			}
		}
		// mark all the vertices reachable from maxPosVer and maxPosVer as visited 
		// and update the number of visited vertices
		adjSize -= mark_visited(adj, visited, maxPosVer, 0);
		//increment the number of SCC
		result++;

	}

	return result;
}

int main() {

	// Few test case to check if the number_of_strongly_connected_components function  and its helper functions works. 
	//These are commented since the assignment requires the strongly_connected.cpp file to read input values and output
	//the respective results on the console
	/**************************************************************************************
	//Test 1

	vector< vector<int> > adj1(6, vector<int>());

	adj1[1 - 1].push_back(4 - 1);
	adj1[1 - 1].push_back(2 - 1);

	adj1[2 - 1].push_back(6 - 1);
	adj1[2 - 1].push_back(3 - 1);

	adj1[3 - 1].push_back(5 - 1);

	adj1[5 - 1].push_back(6 - 1);

	adj1[6 - 1].push_back(1 - 1);

	if (number_of_strongly_connected_components(adj1) == 2)
		std::cout << "Test 1 Passed..." << std::endl;
	else
		std::cout << "Test 1 Failed..." << std::endl;

	//Test 2
	vector< vector<int> > adj2(5, vector<int>());

	adj2[2 - 1].push_back(1 - 1);

	adj2[3 - 1].push_back(2 - 1);
	adj2[3 - 1].push_back(1 - 1);

	adj2[4 - 1].push_back(3 - 1);
	adj2[4 - 1].push_back(1 - 1);

	adj2[5 - 1].push_back(2 - 1);
	adj2[5 - 1].push_back(3 - 1);

	if (number_of_strongly_connected_components(adj2) == 5)
		std::cout << "Test 2 Passed..." << std::endl;
	else
		std::cout << "Test 2 Failed..." << std::endl;



	//Test 3
	vector< vector<int> > adj3(4, vector<int>());

	adj3[1 - 1].push_back(2 - 1);

	adj3[4 - 1].push_back(1 - 1);

	adj3[2 - 1].push_back(3 - 1);

	adj3[3 - 1].push_back(1 - 1);

	if (number_of_strongly_connected_components(adj3) == 2)
		std::cout << "Test 3 Passed..." << std::endl;
	else
		std::cout << "Test 3 Failed..." << std::endl;
	
	//Test 4
	vector< vector<int> > adj4(500, vector<int>());

	if (number_of_strongly_connected_components(adj4) == 500)
		std::cout << "Test 4 Passed..." << std::endl;
	else
		std::cout << "Test 4 Failed..." << std::endl;

	**************************************************************************************/
	// The code below was mostly provided as a part of the starter file for the assignment with few modifications
	size_t n, m;
	std::cin >> n >> m;
	vector< vector<int> > adj(n, vector<int>());
	for (size_t i = 0; i < m; i++) {
		int x, y;
		std::cin >> x >> y;
		adj[x - 1].push_back(y - 1);
	}
	std::cout << number_of_strongly_connected_components(adj);


}
