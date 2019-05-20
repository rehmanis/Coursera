"""
Testing suite for functions used in one implementation
of Yathzee game
"""
# http://www.codeskulptor.org/#user46_i4ScIuelhi_93.py
import poc_simpletest
   
def run_suite_gen_all_holds(gen_all_holds):
    """
    Some basic testing code for testing generation of all possible
    dices that can be held in Yahtzee
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    print "running gen_all_holds function test..."
    
    # test the gen_all_hold
    # Test #1.1: hand is empty. Should return a set with one empty tuple
    hand = ()
    poss_holds = gen_all_holds(hand)
    # run the Test #1.1 and compare the expected vs actual output
    suite.run_test(str(len(poss_holds)), str(1), "Test #1.1: gen_all_hold")
    
    # Test #1.2: hand is of length one. Should return a set with two tuples
    hand = (1,)
    poss_holds = gen_all_holds(hand)
    holds_exp = set((),(1,))
    # run the Test #1.2 and compare the expected vs actual output
    suite.run_test(str(len(poss_holds.intersection(holds_exp))), str(0), 
                   "Test #1.2: gen_all_hold")
    
    # Test #1.3: hand values are distinct. Should return a set of length 
    # 2^(lenght of hand)
    hand = (0,1,2)
    poss_holds = gen_all_holds(hand)
    holds_exp = set((), (0,), (1,), (2,), (0,1), (0,2), (1,2), (0,1,2))
    # run the Test #1.3 and compare the expected vs actual output
    suite.run_test(str(len(poss_holds.intersection(holds_exp))), str(0), 
                   "Test #1.3: gen_all_hold")
    
    # Test #1.4: hand values are all same.
    hand = (1,1,1)
    poss_holds = gen_all_holds(hand)
    holds_exp = set((), (1,), (1,1), (1,1,1))
    # run the Test #1.4 and compare the expected vs actual output
    suite.run_test(str(len(poss_holds.intersection(holds_exp))), str(0), 
                   "Test #1.4: gen_all_hold")
    
    # Test #1.5: hand values have some distinct and some repeated values.
    hand = (1,1,1,2,5)
    poss_holds = gen_all_holds(hand)
    holds_exp = set((), (1,), (2,), (5,), (1,1), (1,2), (1,5), (2,5), 
                    (1,1,1), (1,1,2), (1,1,5), (1,2,5), (1,1,1,2), 
                    (1,1,1,5), (1,1,2,5), (1,1,2,5))
    # run the Test #1.5 and compare the expected vs actual output
    suite.run_test(str(len(poss_holds.intersection(holds_exp))), str(0), 
                   "Test #1.5: gen_all_hold")
    
    # report number of tests and failures
    suite.report_results()
    print
     
def run_suite_score(score):
    """
    Some basic testing code for testing score function 
    for the Yahtzee dice game
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite() 
    
    print "running score function test..."
    
    # test the score function of Yahtzee 
    # Test #2.1: hand is empty. Should return a score zero
    hand = ()
    max_score = score(hand)
    # run the Test #2.1 and compare the expected vs actual output
    suite.run_test(str(max_score), str(0), "Test #2.1: score")
    
    # Test #2.2: hand has one value. Should return this value
    hand = (4,)
    max_score = score(hand)
    # run the Test #2.2 and compare the expected vs actual output
    suite.run_test(str(max_score), str(4), "Test #2.2: score")
    
    # Test #2.3: hand has all same values. Should return this 
    # value time its number of occurances
    hand = (4,4,4,4)
    max_score = score(hand)
    # run the Test #2.3 and compare the expected vs actual output
    suite.run_test(str(max_score), str(16), "Test #2.3: score")
    
    # Test #2.4: hand some repeated values. Should return this 
    # maxim value in the hnad times its number of occurances
    hand = (1,2,2,2,3,6,6)
    max_score = score(hand)
    # run the Test #2.4 and compare the expected vs actual output
    suite.run_test(str(max_score), str(12), "Test #2.4: score")
    
    # report number of tests and failures
    suite.report_results()
    print 
    
def run_suite_expected_value(expected_value):
    """
    Some basic testing code for expected value function 
    to be used in best strategy for play a Yahtzee game
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    print "running expected_value function test..."
    
    # test the exptected_value
    # Test #1.1: no die is held and number of free dice to roll
    # is zero. Should return zero expected value
    held_die = ()
    num_die_sides = 6
    num_free_dice = 0
    exp_value = expected_value(held_die, num_die_sides, num_free_dice)
    # run the Test #1.1 and compare the expected vs actual output
    suite.run_test(str(exp_value), str(0.0), "Test #1.1: expected_value")
    
    # Test #1.2: one die is held and number of free dice to roll
    # is zero. Should return that value of that die
    held_die = (1,)
    num_die_sides = 6
    num_free_dice = 0
    exp_value = expected_value(held_die, num_die_sides, num_free_dice)
    # run the Test #1.2 and compare the expected vs actual output
    suite.run_test(str(exp_value), str(1.0), "Test #1.2: expected_value")
    
    # Test #1.3: no die is held and number of free dice to roll
    # is 1. Should return that expected value of rolling all 
    # possible combination of 1 die which for a 6 sided die
    # is 3.5
    held_die = ()
    num_die_sides = 6
    num_free_dice = 1
    exp_value = expected_value(held_die, num_die_sides, num_free_dice)
    # run the Test #1.3 and compare the expected vs actual output
    suite.run_test(str(exp_value), str(3.5), "Test #1.3: expected_value")
    
    # Test #1.4: one die of value 3 with 6 sides is held and number 
    # of free dice to roll is 1. Should return the expected value 
    # calculated as follows:
    # 1/6 * score(1,3)+ 1/6 * score(2,3) + 1/6 * score(3,3) +...
    # ...+ 1/6 * score (3,6) 
    # = 1/6 * 3 + 1/6 * 3 + 1/6 * 6 +...+ 1/6 * 6 = 4.5
    held_die = (3,)
    num_die_sides = 6
    num_free_dice = 1
    exp_value = expected_value(held_die, num_die_sides, num_free_dice)
    # run the Test #1.4 and compare the expected vs actual output
    suite.run_test(str(exp_value), str(4.5), "Test #1.4: expected_value")
    
    # Test #1.5: two dies with value 2 with 6 sides is held and number 
    # of free dice to roll is 2. Should return the expected value 
    # calculated as follows:
    # 1/36 * score(1,1,2,2) + 1/36 * score(1,2,2,2) + 1/36 * score(1,2,2,3)
    # +...+ 1/36 * score(1,2,2,6) + 1/36 * score(1,2,2,2) +
    # 1/36 * score(2,2,2,2) + 1/36 * score(2,2,2,3) +...
    # = sum of all 36 values
    held_die = (2,2)
    num_die_sides = 6
    num_free_dice = 2
    exp_value = expected_value(held_die, num_die_sides, num_free_dice)
    # run the Test #1.5 and compare the expected vs actual output
    suite.run_test(str(round(exp_value,3)), str(5.833), "Test #1.5: expected_value")
    
    # report number of tests and failures
    suite.report_results()
    print 
    
