"""
Contains the answers to all the questions for 
Application #3 - Comparision of Clustering Algorithm
"""

import random
import copy
import matplotlib.pyplot as plt
import time
import alg_cluster
import alg_clusters_matplotlib as clust_plt
import alg_project3_solution as pj3_sol
import alg_project3_viz as pj3_viz

######################################################
##### Code for Q1 Solution #####
# Q1: Write a function gen_random_clusters(num_clusters) that creates 
# a list of clusters where each cluster in this list corresponds to one 
# randomly generated point in the square with corners (+/-1,+/-1). Use 
# this function and your favorite Python timing code to compute the 
# running times of the functions slow_closest_pair and fast_closest_pair 
# for lists of clusters of size 2 to 200. Once you have computed the running 
# times for both functions, plot the result as two curves combined in a single 
# plot. (Use a line plot for each curve.) The horizontal axis for your plot 
# should be the the number of initial clusters while the vertical axis should 
# be the running time of the function in seconds. Please include a legend in 
# your plot that distinguishes the two curves.

def gen_random_clusters(num_clusters):
    """[summary]
    
    Arguments:
        num_clusters {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """

    # initialize the cluster list to be returned
    cluster_lst = num_clusters * [0]

    for idx in range(num_clusters):
        # generate a random point between -1 and 1
        horz_center = random.uniform(-1.0, 1.0)
        vert_center = random.uniform(-1.0, 1.0)
        # create the cluster and add it to the list
        cluster_lst[idx] = alg_cluster.Cluster(set(), horz_center, vert_center, 1, 0)

    return cluster_lst

# intialize the range of cluster size to be used 
clust_lens = range(2, 200)
# intialize the fast and slow pair function times 
time_slow_closest = []
time_fast_closest = []

# clsts = gen_random_clusters(4)
# print len(clsts)
# print pj3_sol.slow_closest_pair(clsts)

# calcualte the time to run the slow and fast functions for the closest pair
for clust_len in clust_lens:

    # generate the cluster list of size clust_lsn
    cluster_list = gen_random_clusters(clust_len)

    # calculate the closest pair in the cluster using slow algorithm and 
    # store the time it takes to run the function for given cluster size
    start = time.time()
    pj3_sol.slow_closest_pair(cluster_list)
    end = time.time()
    time_slow_closest.append((end - start))
    # calculate the closest pair in the cluster using fast algorithm and 
    # store the time it takes to run the function for given cluster size
    start = time.time()
    pj3_sol.fast_closest_pair(cluster_list)
    end = time.time()
    time_fast_closest.append((end - start))

# plot the graphs of resilience vs number of nodes removed for each of the 3 graphs
#plt.figure(1)
plt.plot(clust_lens, time_slow_closest, '-b', label = 'slow_closest_pair')
plt.plot(clust_lens, time_fast_closest, '-k', label = 'fast_closest_pair')
plt.title('slow vs fast runtime of closest pair function in Visual Studio' )
plt.xlabel('length of clusters')
plt.ylabel('run times[sec]')
plt.legend(loc = 'upper left')
plt.xlim(2, 200)
plt.ylim(0, None)
plt.grid()
plt.show()
# uncommet to save the plot 
#plt.savefig("Q1_closest_pair_comparision.png")


######################################################
# ##### Code for Q2 Solution #####
# Use alg_project3_viz to create an image of the 15 clusters generated by applying 
# hierarchical clustering to the 3108 county cancer risk data set. You may submit 
# an image with the 3108 counties colored by clusters or an enhanced visualization 
# with the original counties colored by cluster and linked to the center of their 
# corresponding clusters by lines. You can generate such an enhanced plot using our
# alg_clusters_matplotlib code by modifying the last parameter of plot_clusters to be
# True. Note that plotting only the resulting cluster centers is not acceptable

# load the data
data_table = pj3_viz.load_data_table(pj3_viz.DATA_3108_URL)

# generate cluster from the data
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

# create a deep copy since hierarchical_clustering modifies the references to the list
singleton_list_cpy = copy.deepcopy(singleton_list) 

# form clusters based on hierarchical clustering algorithm
cluster_list = pj3_sol.hierarchical_clustering(singleton_list_cpy, 15)
print "Displaying", len(cluster_list), "hierarchical clusters"    

# generate the image for the 15 clusters formed using hierarchical clustering algorithm
clust_plt.plot_clusters(data_table, cluster_list, True)

######################################################
##### Code for Q3 Solution #####
# Use alg_project3_viz to create an image of the 15 clusters generated by applying 5 
# iterations of k-means clustering to the 3108 county cancer risk data set. You may 
# submit an image with the 3108 counties colored by clusters or an enhanced visualization 
# with the original counties colored by cluster and linked to the center of their corresponding 
# clusters by lines. As in Project 3, the initial clusters should correspond to the 15 counties 
# with the largest populations.

# form clusters based on k-mean clustering algorithm
cluster_list = pj3_sol.kmeans_clustering(singleton_list, 15, 5)
print "Displaying", len(cluster_list), "k-mean clusters" 

clust_plt.plot_clusters(data_table, cluster_list, True)

######################################################
##### Q4 Solution #####
# Which clustering method is faster when the number of output clusters is either a small 
# fixed number or a small fraction of the number of input clusters? Provide a short 
# explanation in terms of the asymptotic running times of both methods. You should assume 
# that hierarchical_clustering uses fast_closest_pair and that k-means clustering always 
# uses a small fixed number of iterations.
#
# Ans: let k = number of clusters
#          n = size of the input cluster_list
#          q = number of iterations (for k-mean clustering)

# Then for hierarchical clustering, the time complexity is O((n - k) * (n * logn + n * (logn)^2)
# which is ~ O(n^2 * (logn)^2) if k is small compared to n as stated in the above question

# On the other hand, the time complexity of k-mean clustering is ~ O(q * n * k). Since k is small
# compared to n and q is also a small fixed number, time complexity is O(n) which is much more
# efficient than heirarchiacl clustering 

######################################################
##### Q5 Solution #####
# Use alg_project3_viz to create an image of the 9 clusters generated by applying hierarchical 
# clustering to the 111 county cancer risk data set. You may submit an image with the 111 
# counties colored by clusters or an enhanced visualization with the original counties colored 
# by cluster and linked to the center of their corresponding clusters by lines.

# load the data
data_table = pj3_viz.load_data_table(pj3_viz.DATA_111_URL)

# generate cluster from the data
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

# create a deep copy since hierarchical_clustering modifies the references to the list
singleton_list_cpy = copy.deepcopy(singleton_list) 
# form clusters based on hierarchical clustering algorithm
cluster_list_hierarc = pj3_sol.hierarchical_clustering(singleton_list_cpy, 9)  

# generate the image for the 9 clusters formed using hierarchical clustering algorithm
print "Displaying", len(cluster_list_hierarc), "hierarchical clusters"  
clust_plt.plot_clusters(data_table, cluster_list_hierarc, True)

######################################################
##### Q6 Solution #####
# Use alg_project3_viz to create an image of the 9 clusters generated by applying 5 
# iterations of k-means clustering to the 111 county cancer risk data set. You may 
# submit an image with the 111 counties colored by clusters or an enhanced visualization 
# with the original counties colored by cluster and linked to the center of their 
# corresponding clusters by lines. As in Project 3, the initial clusters should correspond 
# to the 9 counties with the largest populations.

# form clusters based on k-mean clustering algorithm
cluster_list_kmean = pj3_sol.kmeans_clustering(singleton_list, 9, 5)

# generate the image for the 9 clusters formed using k-means clustering algorithm
print "Displaying", len(cluster_list_hierarc), "k-mean clusters" 
clust_plt.plot_clusters(data_table, cluster_list_kmean, True)

######################################################
##### Q7 Solution #####
# Write a function compute_distortion(cluster_list) that takes a list of clusters and 
# uses cluster_error to compute its distortion. Now, use compute_distortion to compute 
# the distortions of the two clusterings in questions 5 and 6

def compute_distortion(cluster_list, data_table):

    distortion = sum([cluster.cluster_error(data_table) for cluster in cluster_list])

    return distortion

print compute_distortion(cluster_list_hierarc, data_table)
print compute_distortion(cluster_list_kmean, data_table)

######################################################
##### Q8 Solution #####
# Examine the clusterings generated in Questions 5 and 6. In particular, focus your 
# attention on the number and shape of the clusters located on the west coast of the USA.
# Describe the difference between the shapes of the clusters produced by these two methods 
# on the west coast of the USA. What caused one method to produce a clustering with a much 
# higher distortion? To help you answer this question, you should consider how k-means 
# clustering generates its initial clustering in this case.
#
# Ans: For the k-mean clustering(Figure 5) we can see that the 3 cluster centers are located 
# in the california region (one in northern while two in southern region) while of the 3 
# centers for the hierarchical clustering one is located in Washington state  and two in the 
# california region. The high distortion for the k-mean is due to the fact that the counties 
# in the cluster with center in the northern California is distrbuted in Washington and 
# southern California i.e the counties are much further than the center. The difference between 
# the distortion values is becauses the intial clustering method for k-mean involves clustering 
# around counties with highest population. Due to this all 3 counties(3 largest circles are black 
# and pink) in the southern California were included in the intial clustering while none from 
# Washington, Oregon or Northern California was selected. Thus this resulted in relatively 
# higher distortion.

######################################################
##### Q9 Solution #####
# Based on your answer to Question 8, which method (hierarchical clustering or k-means 
# clustering) requires less human supervision to produce clusterings with relatively 
# low distortion?
#
# Ans: based on Q8, we say that hierarchical clustering requires less human supervision
# as it requires only choosing the number of ouput clusters. While on the other hand
# for k-mean we need a good choice of the intial cluster centers.

######################################################
##### Q10 Solution #####

hierarc_distortion = 15 * [0]
kmean_distortion = 15 * [0]
num_clusters_range = range(20, 5, -1)

## do the calculations for 111 data set
# load the data
data_table = pj3_viz.load_data_table(pj3_viz.DATA_111_URL)

# generate cluster from the data
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

singleton_list_cpy = copy.deepcopy(singleton_list) 

for num_clusters in num_clusters_range:
    cluster_list_hierarc = pj3_sol.hierarchical_clustering(singleton_list_cpy, num_clusters)
    cluster_list_kmean = pj3_sol.kmeans_clustering(singleton_list, num_clusters, 5)
    hierarc_distortion[num_clusters - 6] = compute_distortion(cluster_list_hierarc, data_table)
    kmean_distortion[num_clusters - 6] = compute_distortion(cluster_list_kmean, data_table)   

# reverse the num_cluster_range
num_clusters_range.reverse()

# plot the graphs for distortion for two clustering method for 111 counties
#plt.figure(2)
plt.plot(num_clusters_range, kmean_distortion, '-b', label = 'kmean')
plt.plot(num_clusters_range, hierarc_distortion, '-k', label = 'hierarchical')
plt.title('distortion for kmean vs hierarchical clustering for 111 counties' )
plt.xlabel('number of clusters')
plt.ylabel('distortion')
plt.legend(loc = 'upper right')
plt.xlim(6, 20)
plt.ylim(0, None)
plt.grid()
plt.show()

## do the calculations for 290 data set
# load the data
data_table = pj3_viz.load_data_table(pj3_viz.DATA_290_URL)

# generate cluster from the data
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

num_clusters_range = range(20, 5, -1)
singleton_list_cpy = copy.deepcopy(singleton_list) 

for num_clusters in num_clusters_range:
    cluster_list_hierarc = pj3_sol.hierarchical_clustering(singleton_list_cpy, num_clusters)
    cluster_list_kmean = pj3_sol.kmeans_clustering(singleton_list, num_clusters, 5)
    hierarc_distortion[num_clusters - 6] = compute_distortion(cluster_list_hierarc, data_table)
    kmean_distortion[num_clusters - 6] = compute_distortion(cluster_list_kmean, data_table)   

# reverse the num_cluster_range
num_clusters_range.reverse()

# plot the graphs for distortion for two clustering method for 290 counties
#plt.figure(3)
plt.plot(num_clusters_range, kmean_distortion, '-b', label = 'kmean')
plt.plot(num_clusters_range, hierarc_distortion, '-k', label = 'hierarchical')
plt.title('distortion for kmean vs hierarchical clustering for 290 counties' )
plt.xlabel('number of clusters')
plt.ylabel('distortion')
plt.legend(loc = 'upper right')
plt.xlim(6, 20)
plt.ylim(0, None)
plt.grid()
plt.show()

## do the calculations for 896 data set
# load the data
data_table = pj3_viz.load_data_table(pj3_viz.DATA_896_URL)

# generate cluster from the data
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

num_clusters_range = range(20, 5, -1)
singleton_list_cpy = copy.deepcopy(singleton_list) 

for num_clusters in num_clusters_range:
    cluster_list_hierarc = pj3_sol.hierarchical_clustering(singleton_list_cpy, num_clusters)
    cluster_list_kmean = pj3_sol.kmeans_clustering(singleton_list, num_clusters, 5)
    hierarc_distortion[num_clusters - 6] = compute_distortion(cluster_list_hierarc, data_table)
    kmean_distortion[num_clusters - 6] = compute_distortion(cluster_list_kmean, data_table)   

# reverse the num_cluster_range
num_clusters_range.reverse()

# plot the graphs for distortion for two clustering method for 290 counties
#plt.figure(3)
plt.plot(num_clusters_range, kmean_distortion, '-b', label = 'kmean')
plt.plot(num_clusters_range, hierarc_distortion, '-k', label = 'hierarchical')
plt.title('distortion for kmean vs hierarchical clustering for 896 counties' )
plt.xlabel('number of clusters')
plt.ylabel('distortion')
plt.legend(loc = 'upper right')
plt.xlim(6, 20)
plt.ylim(0, None)
plt.grid()
plt.show()

######################################################
##### Q11 Solution #####
# For each data set (111, 290, and 896 counties), does one clustering method consistently 
# produce lower distortion clusterings when the number of output clusters is in the range 
# 6 to 20? Is so, indicate on which data set(s) one method is superior to the other.
#
# Ans: for 111 counties, hierarchical clustering consistently produces less clusteriing
# For other two data set, there is no one method that consistently produces lower distorion