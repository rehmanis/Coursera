"""
Yahtzee dice game fuction implmentation
for determining optimal strategy of playing
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: sorted tuple representing full yahtzee hand

    Returns an integer score 
    """
    # initialize the local variables
    max_score = 0
    idx = 0
    # iterate over the hand
    while idx < len(hand):
        # find number of occurances for the value at current index
        # in hand
        num_occur = hand.count(hand[idx])
        # update the maximal score if conidition is met
        if num_occur * hand[idx] > max_score:
            max_score = num_occur * hand[idx]
        # bipass all occurances of the current value in hand to 
        # the next index with a different value
        idx += num_occur
      
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # initialize local variables
    exp_score = 0
    # calculate all dice outcomes that can be rolled on a single die
    dice_outcomes = range(1, num_die_sides + 1)
    # calculate all possible combination dice that can be rolled
    # for num_free_dice
    poss_rolls = gen_all_sequences(dice_outcomes, num_free_dice)
    # iterate over all of these combinations and calculate the
    # expected score on concatenated held dice and
    # current possible dice roll combination
    for roll in poss_rolls:
        temp_roll = sorted(list(roll)+list(held_dice))
        exp_score += (1.0/((num_die_sides)**num_free_dice) * score(tuple(temp_roll)))
    
    return exp_score


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand in the form of sorted tuple

    Returns a set of tuples, where each tuple is dice to hold
    """
    # initialize local variables
    ans = set([()])
    # interate over all hand items
    for hand_item in hand:
        # for each possible dice hold combination for the hand 
        # already added, calculate a new hold combination by 
        # adding the current hand_item to it
        for hold in set(ans):
            new_hold = list(hold)
            new_hold.append(hand_item)
            ans.add(tuple(new_hold))
    return ans
            


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand in the form of sorted tuple
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    # initial local variables
    max_exp_score = 0
    # generate all possible holds
    poss_holds = gen_all_holds(hand)
    # iterate over all holds and find the max_exp_score
    # and the corresponding dice to hold
    for hold in poss_holds:
        curr_hold_exp_score = expected_value(hold, num_die_sides, 
                                             len(hand) - len(hold))
        if  curr_hold_exp_score > max_exp_score:
            max_exp_score = curr_hold_exp_score
            max_exp_hold = hold

    return (max_exp_score, max_exp_hold)

###################################################################
# example function call to strategy function 
# uncomment to run it
###################################################################
#def run_example():
#    """
#    Compute the dice to hold and expected score for an example hand
#    """
#    num_die_sides = 6
#    hand = (2,2)
#    hand_score, hold = strategy(hand, num_die_sides)
#    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
#    
#    
#run_example()


##################################################################
# uncomment the below functions to run the test suit for the above
# functions
##################################################################
#import user46_i4ScIuelhi_91 as poc_yahtzee_testsuite
#poc_yahtzee_testsuite.run_suite_gen_all_holds(gen_all_holds)
#poc_yahtzee_testsuite.run_suite_score(score)
#poc_yahtzee_testsuite.run_suite_expected_value(expected_value)


    
    



