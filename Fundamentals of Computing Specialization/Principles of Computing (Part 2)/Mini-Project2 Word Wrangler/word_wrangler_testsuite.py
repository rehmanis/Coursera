"""
Testing suite for functions used in one implementation
of word wrangler game
"""

import poc_simpletest as simpletest
import user46_5gpKzUvHYk_75 as wrangler

class TestWordWangler():
    """
    function that tests the remove_duplicate function
    of the word wrangler game mini-project
    """
    def test_remove_duplicates(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running remove_duplicate function test..."

        # Test #1.1: list is empty. Should return an empty list
        in_lst = []
        out_lst_actual = wrangler.remove_duplicates(in_lst)
        out_lst_exp = []
        # run the Test #1.1 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #1.1: remove_duplicates")
        # Test #1.2: list has one element. Should return same list
        in_lst = [1]
        out_lst_actual = wrangler.remove_duplicates(in_lst)
        out_lst_exp = [1]
        # run the Test #1.2 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #1.2: remove_duplicates")
        # Test #1.3: list has all same elements. Should return list
        # of length 1
        in_lst = [2, 2, 2]
        out_lst_actual = wrangler.remove_duplicates(in_lst)
        out_lst_exp = [2]
        # run the Test #1.3 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #1.3: remove_duplicates")
        # Test #1.4: list has all same elements at the end of the
        # list
        in_lst = [1, 2, 3, 3, 3]
        out_lst_actual = wrangler.remove_duplicates(in_lst)
        out_lst_exp = [1, 2, 3]
        # run the Test #1.4 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #1.4: remove_duplicates")
        
        # Test #1.5: list has some duplicates at the beginning 
        # of the list
        in_lst = [0, 0, 1, 3, 3, 7]
        out_lst_actual = wrangler.remove_duplicates(in_lst)
        out_lst_exp = [0, 1, 3, 7]
        # run the Test #1.5 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #1.5: remove_duplicates")
        
        # Test #1.6: list has mulitple duplicates
        in_lst = [0, 0, 1, 3, 3, 7, 8, 8, 15, 15, 15, 15, 21]
        out_lst_actual = wrangler.remove_duplicates(in_lst)
        out_lst_exp = [0, 1, 3, 7, 8, 15, 21]
        # run the Test #1.6 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #1.6: remove_duplicates")


        # report number of tests and failures
        suite.report_results()
        print 
        
    """
    function that tests the interesct function
    of the word wrangler game mini-project
    """
    def test_intersect(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running intersect function test..."

        # Test #2.1: input lists are empty. Should return 
        # an empty list
        in_lst1 = []
        in_lst2 = []
        out_lst_actual = wrangler.intersect(in_lst1, in_lst2)
        out_lst_exp = []
        # run the Test #2.1 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #2.1: intersect")
        
        # Test #2.2: both input list have one elements with no
        # common value
        # an empty list
        in_lst1 = [1]
        in_lst2 = [2]
        out_lst_actual = wrangler.intersect(in_lst1, in_lst2)
        out_lst_exp = []
        # run the Test #2.2 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #2.2: intersect")
        
        # Test #2.3: both input list have one elements with of same value
        # an empty list
        in_lst1 = [1]
        in_lst2 = [1]
        out_lst_actual = wrangler.intersect(in_lst1, in_lst2)
        out_lst_exp = [1]
        # run the Test #2.3 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #2.3: intersect")
        
        
        # Test #2.4: both input list have multiple elements
        # with one common value
        in_lst1 = [1, 2, 10, 15]
        in_lst2 = [4, 7, 10]
        out_lst_actual = wrangler.intersect(in_lst1, in_lst2)
        out_lst_exp = [10]
        # run the Test #2.4 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #2.4: intersect")
        
        # Test #2.5: one input list is a subset of the other list
        in_lst1 = [1, 2, 10, 15, 30]
        in_lst2 = [2, 10, 15]
        out_lst_actual = wrangler.intersect(in_lst1, in_lst2)
        out_lst_exp = [2, 10, 15]
        # run the Test #2.5 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #2.5: intersect")
        
        # Test #2.6: some random input list combination
        in_lst1 = [1, 2, 10, 15, 30, 33, 40, 100, 200, 300]
        in_lst2 = [2, 10, 15, 17, 19, 300]
        out_lst_actual = wrangler.intersect(in_lst1, in_lst2)
        out_lst_exp = [2, 10, 15, 300]
        # run the Test #2.6 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #2.6: intersect")


        # report number of tests and failures
        suite.report_results()
        print 
    
        
    """
    function that tests the merge function
    of the word wrangler game mini-project
    """
    def test_merge(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running merge function test..."

        # Test #3.1: both input lists are empty. Should return 
        # an empty list
        in_lst1 = []
        in_lst2 = []
        out_lst_actual = wrangler.merge(in_lst1, in_lst2)
        out_lst_exp = []
        # run the Test #3.1 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #3.1: merge")
        # Test #3.2: first list is empty and while second has
        # one element
        in_lst1 = []
        in_lst2 = [1]
        out_lst_actual = wrangler.merge(in_lst1, in_lst2)
        out_lst_exp = [1]
        # run the Test #3.2 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #3.2: merge")
        # Test #3.3: first list has one element while second
        # is empty
        # of length 1
        in_lst1 = [2]
        in_lst2 = []
        out_lst_actual = wrangler.merge(in_lst1, in_lst2)
        out_lst_exp = [2]
        # run the Test #3.3 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #3.3: merge")
        # Test #3.4: both lists are equal i.e have same
        # elements
        in_lst1 = [1, 2, 3]
        in_lst2 = [1, 2, 3]
        out_lst_actual = wrangler.merge(in_lst1, in_lst2)
        out_lst_exp = [1, 1, 2, 2, 3, 3]
        # run the Test #3.4 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #3.4: merge")
        
        # Test #3.5: first list has more elements than second list
        # with some duplicates
        in_lst1 = [0, 0, 1, 3]
        in_lst2 = [0, 5, 10]
        out_lst_actual = wrangler.merge(in_lst1, in_lst2)
        out_lst_exp = [0, 0, 0, 1, 3, 5, 10]
        # run the Test #3.5 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #3.5: merge")
        
        # Test #3.6: first list has less elements than second list
        in_lst1 = [5, 10]
        in_lst2 = [2, 5, 11, 40, 41, 50]
        out_lst_actual = wrangler.merge(in_lst1, in_lst2)
        out_lst_exp = [2, 5, 5, 10, 11, 40, 41, 50]
        # run the Test #3.6 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #3.6: merge")
        
        # Test #3.7: some random combination
        in_lst1 = [11, 12, 15, 15, 15]
        in_lst2 = [2, 15, 15, 30]
        out_lst_actual = wrangler.merge(in_lst1, in_lst2)
        out_lst_exp = [2, 11, 12, 15, 15, 15, 15, 15, 30]
        # run the Test #3.7 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #3.7: merge")


        # report number of tests and failures
        suite.report_results()
        print 
        
    """
    function that tests the merge_sort function
    of the word wrangler game mini-project
    """
    def test_merge_sort(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running merge_sort function test..."

        # Test #4.1: input list is empty. Should return an empty list
        in_lst = []
        out_lst_actual = wrangler.merge_sort(in_lst)
        out_lst_exp = []
        # run the Test #4.1 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #4.1: merge_sort")
        # Test #4.2: input list has one element. Should return same list
        in_lst = [1]
        out_lst_actual = wrangler.merge_sort(in_lst)
        out_lst_exp = [1]
        # run the Test #4.2 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #4.2: merge_sort")
        # Test #4.3: input list has all same elements. Should return the
        # list in same order as input list
        in_lst = [1, 1, 1]
        out_lst_actual = wrangler.merge_sort(in_lst)
        out_lst_exp = [1, 1, 1]
        # run the Test #4.3 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #4.3: merge_sort")
        # Test #4.4: input list is in descending order. Should
        # return list in ascending order
        in_lst = [11, 5, 3, 2, 2]
        out_lst_actual = wrangler.merge_sort(in_lst)
        out_lst_exp = [2, 2, 3, 5, 11]
        # run the Test #4.4 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #4.4: merge_sort")
        
        # Test #4.5: input list is randomly unordered. Should
        # return a list in ascending order
        in_lst = [1, 11, 2, 6, 3, 0, -1, 100]
        out_lst_actual = wrangler.merge_sort(in_lst)
        out_lst_exp = [-1, 0, 1, 2, 3, 6, 11, 100]
        # run the Test #4.5 and compare the expected vs actual output
        suite.run_test(str(out_lst_actual), str(out_lst_exp), 
                       "Test #4.5: merge_sort")

        # report number of tests and failures
        suite.report_results()
        print         
        
        """
        helper function to check if all elements of the
        list are same
        """
        
    """
    function that tests gen_all_strings function
    of the word wrangler game mini-project
    """
    def test_gen_all_strings(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running gen_all_strings function test..."

        # Test #5.1: input string is empty. Should return empty string
        in_string = ""
        out_str_lst_actual = wrangler.gen_all_strings(in_string)
        out_str_lst_exp = [""]
        # run the Test #5.1 and compare the expected vs actual output
        suite.run_test(str(out_str_lst_actual), str(out_str_lst_exp), 
                       "Test #5.1: gen_all_strings")
        # Test #5.2: input string has one element. 
        in_string = "a"
        out_str_lst_actual = wrangler.gen_all_strings(in_string)
        out_str_lst_exp = ["", "a"]
        # run the Test #5.2 and compare the expected vs actual output
        suite.run_test(str(out_str_lst_actual), str(out_str_lst_exp), 
                       "Test #5.2: gen_all_strings") 
        # Test #5.3: input string has distinct characters. 
        in_string = "abc"
        out_str_lst_actual = wrangler.gen_all_strings(in_string)
        out_str_lst_exp = ['', 'c', 'b', 'bc', 'cb', 'a', 'ac', 'ca', 
                           'ab', 'ba', 'abc', 'bac', 'bca', 'acb', 
                           'cab', 'cba']
        # run the Test #5.3 and compare the expected vs actual output
        suite.run_test(str(out_str_lst_actual), str(out_str_lst_exp), 
                       "Test #5.3: gen_all_strings")
        # Test #5.4: input string has duplicate characters. 
        in_string = "aab"
        out_str_lst_actual = wrangler.gen_all_strings(in_string)
        out_str_lst_exp = ['', 'b', 'a', 'ab', 'ba', 'a', 'ab', 'ba',
                           'aa', 'aa', 'aab', 'aab', 'aba', 'aba', 
                           'baa', 'baa']
        # run the Test #5.4 and compare the expected vs actual output
        suite.run_test(str(out_str_lst_actual), str(out_str_lst_exp), 
                       "Test #5.4: gen_all_strings")         
        
        # report number of tests and failures
        suite.report_results()
        print          
        
    
# test all functions of the word wangler pini-project
word_wangler = TestWordWangler()
word_wangler.test_remove_duplicates()
word_wangler.test_intersect()
word_wangler.test_merge()
word_wangler.test_merge_sort()
word_wangler.test_gen_all_strings()

