"""
All answers to questions in Application #4 -
Applications to Genomics and Beyond
"""

import random
import matplotlib.pyplot as plt
import alg_application4_provided as alg_app4_prov
import alg_project4_solution as alg_proj4_sol

##########################################################################
# Solution Q1

# Q1: First, load the files HumanEyelessProtein and FruitflyEyelessProtein 
# using the provided code. These files contain the amino acid sequences that 
# form the eyeless proteins in the human and fruit fly genomes, respectively. 
# Then load the scoring matrix PAM50 for sequences of amino acids. This scoring
# matrix is defined over the alphabet {A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,Y,V,B,Z,X,-} 
# which represents all possible amino acids and gaps (the "dashes" in the alignment).
# Next, compute the local alignments of the sequences of HumanEyelessProtein and 
# FruitflyEyelessProtein using the PAM50 scoring matrix and enter the score and 
# local alignments for these two sequences below. Be sure to clearly distinguish 
# which alignment is which and include any dashes ('-') that might appear in the 
# local alignment.

# load the two amino acid sequences that form the eyeless proteins in the human 
# and fruit fly genomes
human_seq = alg_app4_prov.read_protein(alg_app4_prov.HUMAN_EYELESS_URL)
fly_seq = alg_app4_prov.read_protein(alg_app4_prov.FRUITFLY_EYELESS_URL)

# load their scoring matrix
scoring_matrix = alg_app4_prov.read_scoring_matrix(alg_app4_prov.PAM50_URL)

# compute the local alignments matrix for these 2 sequences
local_align_matrix = alg_proj4_sol.compute_alignment_matrix(human_seq, fly_seq, scoring_matrix, False)

# compute the local alignments and the score for the two sequences
(score_q1, align_human, align_fly) = alg_proj4_sol.compute_local_alignment(human_seq, 
                                                                        fly_seq, scoring_matrix, 
                                                                        local_align_matrix)

print "Q1 Answers: "                                                                        
print "Score: ",score_q1
print "local alignment of human: ", align_human
print "local alignment of fly:   ", align_fly
print 

##########################################################################
# Solution Q2 
# Q2: To continue our investigation, we next consider the similarity of the two 
# sequences in the local alignment computed in Question 1 to a third sequence. 
# The file ConsensusPAXDomain contains a "consensus" sequence of the PAX domain;
# that is, the sequence of amino acids in the PAX domain in any organism. In this 
# problem, we will compare each of the two sequences of the local alignment computed 
# in Question 1 to this consensus sequence to determine whether they correspond to 
# the PAX domain.
#
# Load the file ConsensusPAXDomain. For each of the two sequences of the local 
# alignment computed in Question 1, do the following:
# 
# - Delete any dashes '-' present in the sequence.
# - Compute the global alignment of this dash-less sequence with the ConsensusPAXDomain 
#   sequence.
# - Compare corresponding elements of these two globally-aligned sequences (local vs. 
#   consensus) and compute the percentage of elements in these two sequences that agree.

# load the file ConsensusPAXDomain
pax_domain_seq = alg_app4_prov.read_protein(alg_app4_prov.CONSENSUS_PAX_URL)

# delete the dashes from the 2 local alignments in Q1
hum_nodash_seq = align_human.replace('-', "")

# compute the global alignments matrix for PAX domain and local human alignment seq with no dash
glob_align_mat_hum_pax = alg_proj4_sol.compute_alignment_matrix(pax_domain_seq, hum_nodash_seq, 
                                                                scoring_matrix, True)
                                                        
# compute the global alignment matrix for the PAX domain and local fly alignment seq with no dash
glob_align_mat_fly_pax = alg_proj4_sol.compute_alignment_matrix(pax_domain_seq, align_fly, 
                                                                scoring_matrix, True)

(_, align_pax_hum, align_hum_nodash) = alg_proj4_sol.compute_global_alignment(pax_domain_seq, 
                                                                              hum_nodash_seq, 
                                                                              scoring_matrix, 
                                                                              glob_align_mat_hum_pax)

(_, align_pax_fly, align_fly_nodash) = alg_proj4_sol.compute_global_alignment(pax_domain_seq, 
                                                                              align_fly, 
                                                                              scoring_matrix, 
                                                                              glob_align_mat_fly_pax)

count_pax_hum = 0.0
count_pax_fly = 0.0


for charc_i, charc_j in zip(align_pax_hum, align_hum_nodash):
    if charc_i == charc_j:
        count_pax_hum += 1

print "Q2 Answers: "  
print ("percentage of elments global alignment of local human vs PAX that agree: " +
        str(round(count_pax_hum/len(align_pax_hum) * 100, 2)) + "%")

for charc_i, charc_j in zip(align_pax_fly, align_fly_nodash):
    if charc_i == charc_j:
        count_pax_fly += 1 

print ("percentage of elments global alignment of local fly vs PAX that agree: " +
        str(round(count_pax_fly/len(align_pax_fly) * 100, 2)) + "%")
print

##########################################################################
# Solution Q3
# Q3: Examine your answers to Questions 1 and 2. Is it likely that the level of 
# similarity exhibited by the answers could have been due to chance? In particular, 
# if you were comparing two random sequences of amino acids of length similar to 
# that of HumanEyelessProtein and FruitflyEyelessProtein, would the level of agreement 
# in these answers be likely? To help you in your analysis, there are 23 amino acids 
# with symbols in the string "ACBEDGFIHKMLNQPSRTWVYXZ". Include a short justification 
# for your answer.
#
# Ans: The number of elements matching between each local alignment to the PAX 
# consensus domain is too high to deemed that they matched due to chance.
# 
# For local human vs PAX, 97 out of 133 elements match and the probability
# for all 97 of them to match due to chance would be quite small given than we have
# to randomly choose between 23 alphabets and that the probability of choosing
# an element is equal for all alphabets
#
# The same can be said for the local fly vs PAX where 94 out of the 134 elements
# match

print "Q3 Answers:"
print "length of global alignment of human vs pax: ", len(align_pax_hum)
print "number of elements matching in this global alignment: ", int(count_pax_hum)
print "length of global alignment of fly vs pax: ", len(align_pax_fly)
print "number of elements matching in this global alignment: ", int(count_pax_fly)
print 

##########################################################################
# Solution Q4
#
# Q4: Write a function generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials) 
# that takes as input two sequences seq_x and seq_y, a scoring matrix scoring_matrix, and a 
# number of trials num_trials. This function should return a dictionary scoring_distribution 
# that represents an un-normalized distribution generated by performing the following process 
# num_trials times:
#
# - Generate a random permutation rand_y of the sequence seq_y using random.shuffle().
# - Compute the maximum value score for the local alignment of seq_x and rand_y using the score 
#   matrix scoring_matrix.
# - Increment the entry score in the dictionary scoring_distribution by one.
#
# Use the function generate_null_distribution to create a distribution with 1000 trials using 
# the protein sequences HumanEyelessProtein and FruitflyEyelessProtein (using the PAM50 scoring matrix). 
# Important: Use HumanEyelessProtein as the first parameter seq_x (which stays fixed) and 
# FruitflyEyelessProtein as the second parameter seq_y (which is randomly shuffled) when calling 
# generate_null_distribution. Switching the order of these two parameters will lead to a slightly 
# different answers for question 5 that may lie outside the accepted ranges for correct answers.
# 
# Next, create a bar plot of the normalized version of this distribution using plt.bar in 
# matplotlib (or your favorite plotting tool). (You will probably find CodeSkulptor too slow to 
# do the required number of trials.) The horizontal axis should be the scores and the vertical axis 
# should be the fraction of total trials corresponding to each score. As usual, choose reasonable 
# labels for the axes and title. Note: You may wish to save the distribution that you compute in 
# this Question for later use in Question 5.

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    """
    Takes as input two sequences seq_x and seq_y, a scoring matrix scoring_matrix, and a 
    number of trials num_trials. This function should return a dictionary scoring_distribution 
    that represents an un-normalized distribution generated by performing the following process 
    num_trials times:

    - Generate a random permutation rand_y of the sequence seq_y using random.shuffle().
    - Compute the maximum value score for the local alignment of seq_x and rand_y using the score 
      matrix scoring_matrix.
    - Increment the entry score in the dictionary scoring_distribution by one.    
    
    Arguments:
        seq_x {string} -- a sequence of alphabets representing amino acids
        seq_y {string} -- a sequence of alphabets representing amino acids
        scoring_matrix {dict of dict} -- the scoring matrix for the all alphabet plus "-" combination
        num_trials {integer} -- the number of trial
    
    Returns:
        dict -- a dictionary representing the scoring distribution 
    """

    # initialize the scoring distribution
    scoring_distribution = {}

    for dummy_idx in range(num_trials):
        # generate a random permutation for the seq_y
        rand_y = list(seq_y)
        random.shuffle(rand_y)
        rand_y = "".join(rand_y)

        # compute the local alignments matrix for seq_x and rand_y
        local_align_matrix = alg_proj4_sol.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)

        # compute the local alignment score for the two sequences
        (score, _, _) = alg_proj4_sol.compute_local_alignment(seq_x, rand_y, scoring_matrix, local_align_matrix)

        # increment the entry score in the scoring_distribution
        if scoring_distribution.has_key(score):
            scoring_distribution[score] += 1
        else:
            scoring_distribution[score] = 1        


    return scoring_distribution

# get the scoring distribution for 1000 trial for HumanEyelessProtein and FruitflyEyelessProtein
scoring_dist = generate_null_distribution(human_seq, fly_seq, scoring_matrix, 1000)

sum_of_vals = float(sum(scoring_dist.values()))
norm_values = [value/sum_of_vals for value in scoring_dist.values()]
plt.bar(scoring_dist.keys(), norm_values)
plt.title('Hypothesis testing for 1000 trials for null distribution')
plt.xlabel('Local alignment scores')
plt.ylabel('frequency of scores/fraction of trials')
plt.xlim(None, None)
plt.ylim(None, None)
plt.show()

# ##########################################################################
# Solution Q5
#
# Q5: What are the mean and standard deviation for the distribution that you 
# computed in Question 4?
# What is the z-score for the local alignment for the human eyeless protein vs. 
# the fruitfly eyeless protein based on these values?

# calculate the mean of the distribution
num_trials = 1000.0
mean_mu = sum([key * value for key, value in scoring_dist.items()])/num_trials

# calculate the standard deviation 
sigma = sum([((key - mean_mu) ** 2) * value for key, value in scoring_dist.items()])/num_trials
sigma = sigma ** 0.5

# use mean and standard deviation to calculate the z score
z_score = (score_q1 - mean_mu)/sigma

print "Q5 Answers"
print "mean of the distrubution: ", mean_mu
print "standard deviation of distribution: ", sigma
print "z-score of the distribution: ", z_score
print

##########################################################################
# Solution Q6
#
# Q6: Based on your answers to Questions 4 and 5, is the score resulting from the local 
# alignment of the HumanEyelessProtein and the FruitflyEyelessProtein due to chance? As 
# a concrete question, which is more likely: the similarity between the human eyeless 
# protein and the fruitfly eyeless protein being due to chance or winning the jackpot 
# in an extremely large lottery? Provide a short explanation for your answers
#
# Ans: the z-score is around 100 which means it right at the corner of the bell
# shaped. 1 standard deviation from the mean of around 50 is about 7. And
# we know that 3 standard deviations(sigma) covers about 99% of bell shape, i.e the 
# likelihood of value falling within 3 sigma is high and the probability of
# value to fall outside 3 sigma is  about 1%. The z-score we found tells us that
# the value of the score we found in Q1 is about 100 standard away from mean
# (score of 875 is more than 100 * sigma + mean)
# We can find the exact probality using the z test for normal distribution
# which gives us a probablity on the order of 10^(-2000)
# (https://www.wolframalpha.com/input/?i=Probability+of+100+standard+deviations)
# which is much smaller than the chance of winning a lottery 

##########################################################################
# Solution Q7
#
# Not surprisingly, similarity between pairs of sequences and edit distances between pairs 
# of strings are related. In particular, the edit distance for two strings x and y can be 
# expressed in terms of the lengths of the two strings and their corresponding similarity 
# score as follows: |x| + |y| - score(x, y) where score(x, y) is the score returned by the 
# global alignment of these two strings using a very simple scoring matrix that can be 
# computed using build_scoring_matrix.
# Determine the values for diag_score, off_diag_score, and dash_score such that the score 
# from the resulting global alignment yields the edit distance when substituted into the 
# formula above
#
# Ans: 
# 1-Let x = "ABC" and y = "". Then global alignment will return x' = "ABC" and y' = "---"
#   so |x| = 3 and |y| = 0 and edit distance need 3 substitution operation to subsitute "---"
#   to "ABC" and score(x', y') = |x'| +|y'| - 3 = 0. Therefore, dash_score = 0
#   dash_score = 0

# 2-Let x = "ABC" and y = "ABC". Then global alignment returns the same strings and edit
#   distance need zero operations. Hence score(x, y) = |x| + |y| - 0 = 3 + 3 = 6. Thus
#   diag_score must be 2 for the score of x, y to be 6
#   diag_score = 2

# 3-Let x = "ABC" and y = "ABT". Then global alignment resturns the same strings with
#   total score of score of string "C" and "T" + 2 * diag_score. Hence edit distance needs
#   subsitution od "T" to "C" i.e one operation. Thus we have:
#   score("C", T) + 2 * diag_score = |x| + |y| - 1 
#   off_diag_score = 3 + 3 - 1 - 2 * 2 = 1
#   off_diag_score = 1 

##########################################################################
# Solution Q8
#
# Q8: For this final question, we will implement a simple spelling correction function that 
# uses edit distance to determine whether a given string is the misspelling of a word.
# To begin, load this list of 79339 words. Then, write a function 
# check_spelling(checked_word, dist, word_list) that iterates through word_list and returns 
# the set of all words that are within edit distance dist of the string checked_word.
# Use your function check_spelling to compute the set of words within an edit distance of 
# one from the string "humble" and the set of words within an edit distance of two from the 
# string "firefly".
#

def check_spelling(checked_word, dist, word_list):
    """[summary]
    
    Arguments:
        checked_word {[type]} -- [description]
        dist {[type]} -- [description]
        word_list {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    
    # initialize the set that will contain a list of words within edit distance dist
    # from word_list
    within_dist = set()

    # initalize a set of alphabets
    alphabets = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    # compute the scoring matrix for of scores calculated in Q7
    score_mat = alg_proj4_sol.build_scoring_matrix(alphabets, 2, 1, 0)

    for word in word_list:
        # compute the global alignment matrix
        align_mat = alg_proj4_sol.compute_alignment_matrix(word, checked_word, score_mat, True)

        # compute the global alignment score of the word
        (score, _, _) = alg_proj4_sol.compute_global_alignment(word, checked_word, score_mat, align_mat)

        # add the word to the within_dist set if it edit distance is within edit distance dist
        if (len(word) + len(checked_word) - score) <= dist:
            within_dist.add(word)

    return within_dist

# load the word list
word_list = alg_app4_prov.read_words(alg_app4_prov.WORD_LIST_URL)

# compute the set of word that are within edit distance 1 of string "humble"
with_wrds_humble = check_spelling("humble", 1, word_list)

# compute the set of word that are within edit distance 2 of string "firefly"
with_wrds_firefly = check_spelling("firefly", 2, word_list)

print "Q8 Answers:"
print "words within 1 edit distance of string 'humble': \n", with_wrds_humble
print "words within 2 edit distance of string 'firefly': \n", with_wrds_firefly
