"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    # create a variable to store the new list of no duplicates
    new_lst = []
    # iterate over the length of list1 adding the element to
    # the new_lst if there are duplicates
    for lst_idx in range(len(list1)):
        if (lst_idx < len(list1)-1 and list1[lst_idx+1] != list1[lst_idx]):
            new_lst += [list1[lst_idx]]
        # the last elemnt of the list needs to be added since it
        # will not be added to the new_lst
        elif (lst_idx == len(list1)-1):
            new_lst += [list1[lst_idx]]
    
    return new_lst

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    # initialize the list which will contain the intersection
    inters_lst = []
    # initialize input list indices to move accross the list
    idx_list1 = 0
    idx_list2 = 0
    
    # since input lists are sorted, we can traverse the list
    # in O(n+m) i.e linear time. If current element in
    # list1 is smaller than list2, we move one index forward 
    # in list1. If the current element in list1 is greater than
    # element in list2, we move one index in list2. If they are
    # the same in both lists, we store it in inters_lst and 
    # move one index forward for both list. We continue
    # this until one of the input lists have been completely
    # traversed.
    while idx_list1 < len(list1) and idx_list2 < len(list2):
        if (list1[idx_list1] < list2[idx_list2]):
            idx_list1 += 1
        elif (list1[idx_list1] > list2[idx_list2]):
            idx_list2 += 1
            
        else:
            inters_lst += [list1[idx_list1]]
            idx_list1 += 1
            idx_list2 += 1
                
    return inters_lst

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    # copy the input lists so that the original lists are not 
    # mutated
    copy_list1 = list(list1)
    copy_list2 = list(list2)
    # this will store the merged sorted list 
    new_merge_lst = []
    # pop the elments from list by checking which one is smaller
    # and add the elements in asceding order to the new_merge_lst
    while (len(copy_list1) > 0 and len(copy_list2) > 0):
        if (copy_list1[0] < copy_list2[0]):
            new_merge_lst += [copy_list1.pop(0)]
        else:
            new_merge_lst += [copy_list2.pop(0)]
            
    
    new_merge_lst += copy_list1 + copy_list2
        
    return new_merge_lst
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # check the base case when list is empty or has one element
    # In this case the list1 is alreay sorted so we return it
    if len(list1) == 1 or len(list1) == 0:
        return list1
    # the inductive/recursive case requires us to break the list 
    # into 2, and perform merge sort on these two
    # recursively to get left_half and the right_half. 
    # Once we have two sorted list, we merge them by calling
    # merge function above
    else:
        lst_mid_idx = len(list1)/2
        left_half = merge_sort(list1[ : lst_mid_idx])
        right_half = merge_sort(list1[lst_mid_idx : ])
        return merge(left_half, right_half)
                   

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    # base case is when string is empty
    if len(word) == 0 :
        return [""]
    # recusive case involves performing the gen_all_strings 
    # recursively on the word without the first character
    # and then adding the first character to all possible 
    # locations in all strings in the list of strings
    # made up of string of word characters without
    # the first word character
    else:
        first_char = word[0]
        rest_strings = gen_all_strings(word[1:])
        for string in list(rest_strings):
            string_lst = list(string)
            for str_idx in range(len(string)+1):
                string_lst.insert(str_idx, first_char)
                rest_strings += ["".join(string_lst)]
                string_lst.pop(str_idx)
                
        return rest_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    # the last character in the word is the newline
    # "\n" which is not needed
    return [word[:-1] for word in netfile]

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# lauches the game
run()

    
    