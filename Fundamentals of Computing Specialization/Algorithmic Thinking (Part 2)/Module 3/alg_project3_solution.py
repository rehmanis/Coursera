"""
All the algorithms for Project 3 for closest
pair and clustering 
"""

import alg_cluster

######################################################
# Code for closest pairs of clusters
def slow_closest_pair(cluster_list):
    """
    Uses the brute-force algorithm (O(n^2)) to find the closest pair of clusters in a list
    
    Arguments:
        cluster_list {Cluster} -- a list of Cluster objects
    
    Returns:
        tuple -- returns a closest pair where the pair is represented by the tuple 
                 (dist, idx1, idx2) with idx1 < idx2 where dist is the distance between 
                 the closest pair cluster_list[idx1] and cluster_list[idx2].
    """
    # initialize the tuple that will store the closest pair of cluster distance and index
    (dist, idx1, idx2) = (float("inf"), -1, -1)
    
    for clusteri_idx in range(len(cluster_list)):
        for clusterj_idx in range(len(cluster_list)):
            if (clusteri_idx != clusterj_idx):
                curr_dist = cluster_list[clusteri_idx].distance(cluster_list[clusterj_idx])
                (dist, idx1, idx2) = (min(set([(dist, idx1, idx2), (curr_dist, clusteri_idx, clusterj_idx)]), 
                    key = lambda tup: tup[0]))

    if (idx2 > idx1):
        return (dist, idx1, idx2)
    else:
        return (dist, idx2, idx1)

def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list using fast algorithm 
    [O(n*(logn)^2]
 
    Arguments:
        cluster_list {list} -- list of clusters sorted based on the horizontal distance of 
                               their centers in ascending order
    
    Returns:
        tuple -- tuple of the form (dist, idx1, idx2) where the centers of the clusters
                 cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """

    # base case 
    if len(cluster_list) <= 3:
        (dist, idx1, idx2) = slow_closest_pair(cluster_list)

    # inductive case    
    else:
        # divide the problem in half, solve it and then merge the results from both
        idx_m = len(cluster_list) / 2
        # solve for the left half of the cluster list
        (d_left, idxi_l, idxj_l) = fast_closest_pair(cluster_list[ : idx_m]) 
        # solve for right half of the cluster list
        (d_right, idxi_r, idxj_r) = fast_closest_pair(cluster_list[idx_m : ])
        # find the minimum of the left and right paritiion minimum distances
        (dist, idx1, idx2) = (min(set([(d_left, idxi_l, idxj_l), (d_right, idxi_r + idx_m, idxj_r + idx_m)]), 
            key = lambda tup: tup[0]))
        # find the the horizontal position of the strip's vertical center line i.e the midpoint of the
        # horizontal position of the last element of the left perition and first element of the right parition      
        horiz_center = 0.5 * (cluster_list[idx_m - 1].horiz_center() + cluster_list[idx_m].horiz_center())
        # find the minimum of the minimum distance found earlier and the closest pair in the strip  
        (dist, idx1, idx2) = (min(set([(dist, idx1, idx2), closest_pair_strip(cluster_list, horiz_center, dist)]), 
            key = lambda tup: tup[0]))

    return (dist, idx1, idx2) 

def closest_pair_strip(cluster_list, horiz_center, half_width) :
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Arguments:
        cluster_list {list} -- a list of Cluster objects
        horiz_center {integer} -- the horizontal position of the strip's vertical center line   
        half_width {integer} -- the half the width of the strip (i.e; the maximum horizontal distance
                                that a cluster can lie from the center line)
    
    Returns:
        tuple -- returns a tuple of the form (dist, idx1, idx2) where the centers of the clusters
                 cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist. 
    """

    # store all cluster whose centres are within the vertical strip specified by horiz_center and half_width
    strip_clust = [(cluster_list[clst_idx], clst_idx) for clst_idx in range(len(cluster_list)) 
        if abs(cluster_list[clst_idx].horiz_center() - horiz_center) < half_width ]
    
    # sort the cluster based on their vertical distances
    strip_clust.sort(key = lambda cluster: cluster[0].vert_center())

    # intialize the minimium ditance and their indices
    (dist, idx1, idx2) = (float("inf"), -1, -1)

    # for each cluster inspect the next 3 ones and record the pair of cluster indices that
    # corresponds to closest pair thus found
    for clsti_idx in range(len(strip_clust) - 1):
        for clstj_idx in range(clsti_idx + 1, min((clsti_idx + 4), len(strip_clust))):
            curr_dist = strip_clust[clsti_idx][0].distance(strip_clust[clstj_idx][0])
            (dist, idx1, idx2) = (min(set([(dist, idx1, idx2), 
                (curr_dist, strip_clust[clsti_idx][1], strip_clust[clstj_idx][1])]), key = lambda tup: tup[0]))
    
    # return minimum distance and their indicies (dist, idx1, idx2) where idx1 < idx2 
    if (idx2 > idx1):
        return (dist, idx1, idx2)
    else:
        return (dist, idx2, idx1)

######################################################################
# Code for hierarchical clustering
def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list to have length num_clusters   
    
    Arguments:
        cluster_list {list} -- a list of Cluster objects
        num_clusters {integer} -- integer number of clusters to be made from cluster_list
    
    Returns:
        list -- a list of Cluster objects whose length is num_clusters
    """

    while len(cluster_list) > num_clusters:
        # sort the cluster based on their horizontal distances
        #print cluster_list
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        #print cluster_list
        (dummy_dist, idx1, idx2) = fast_closest_pair(cluster_list)
        cluster_list[idx1].merge_clusters(cluster_list[idx2])
        #print cluster_list
        cluster_list.pop(idx2)

    return cluster_list

######################################################################
# Code for k-means clustering

def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function does not mutate cluster_list to have length num_clusters   
    
    Arguments:
        cluster_list {list} -- a list of Cluster objects
        num_clusters {integer} -- integer number of clusters to be made from cluster_list
        num_iterations {integer} -- number of iterations
    
    Returns:
        list -- a list of Cluster objects whose length is num_clusters
    """
    # compute an initial list of clusters with the property that each cluster consists of 
    # a single county chosen from the set of the num_cluster counties with the largest populations
    cluster_list_cpy = list(cluster_list)
    cluster_list_cpy.sort(key = lambda cluster: cluster.total_population())
    cluster_len = len(cluster_list) 
    old_cluster = cluster_list_cpy[cluster_len - num_clusters : ]
    
    for dummy_idx in range(num_iterations):
        # initialze an empty cluster 
        new_cluster = [alg_cluster.Cluster(set(), 0.0, 0.0, 0, 0) for dummy_i in range(num_clusters)]
        for idx_i in range(cluster_len):
            min_dist = float("inf")
            min_idx = -1
            # find the cluster from old_cluster and its index that is closest to current cluster 
            # in the cluster_list
            for idx_j in range(num_clusters):
                curr_dist = old_cluster[idx_j].distance(cluster_list[idx_i])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    min_idx = idx_j
            # add the cluster to the new_cluster at index = min_idx
            new_cluster[min_idx].merge_clusters(cluster_list[idx_i])

        old_cluster = new_cluster
        
    return new_cluster


