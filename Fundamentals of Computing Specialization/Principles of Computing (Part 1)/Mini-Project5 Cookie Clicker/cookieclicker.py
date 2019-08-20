"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._tot_cookies = 0.0
        self._curr_cookies = 0.0
        self._curr_time = 0.0
        self._curr_cps = 1.0
        # game history has the time, an item that was bought at that time 
        # (or None), the cost of the item, and the total number of cookies 
        # produced by that time.
        self._game_history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        state = ("\n"+"Total cookies: " + str(self._tot_cookies) +
                "\n" + "Current cookies: " + str(self._curr_cookies) + 
                "\n" +"Current time of game: " + str(self._curr_time) +
                "s" + "\n" +"Current CPS: " + str(self._curr_cps) + "\n")                             
                                                 
                                           
        
        return state
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._curr_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._curr_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._curr_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._game_history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        curr_cookies = self.get_cookies()
        if curr_cookies >= cookies :
            return 0.0
        else:
            curr_cps = self.get_cps()
            cookies_needed = cookies - curr_cookies
            time = math.ceil(cookies_needed / curr_cps)
            
        return time
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if (time > 0.0):
            self._curr_time += time
            self._curr_cookies += time * self._curr_cps
            # using self._tot_cookies += self._curr_cookies
            # give incorrect total cookies value since
            # it also adds the earlier cookie value
            self._tot_cookies += time * self._curr_cps 
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if (cost <= self.get_cookies()):
            self._curr_cookies -= cost
            self._curr_cps += additional_cps
            self._game_history.append((self.get_time(), item_name, 
                                       cost, self._tot_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    # make a copy of the build_info object so as not to 
    # mutate it
    build_info_copy = build_info.clone()
    # create a new Clickerstate
    clicker_state = ClickerState()
    # loop until duration has passed
    while (clicker_state.get_time() <= duration):
        # determine which item to buy based on the strategy
        item = strategy(clicker_state.get_cookies(),
                        clicker_state.get_cps(),
                        clicker_state.get_history(),
                        duration - clicker_state.get_time(),
                        build_info_copy)
        # if item is None, then that means no more items
        # can be purchased, and simulation should stop
        if (item == None):
            break
        # find the cost of the item
        item_cost = build_info_copy.get_cost(item)
        #print "item cost: ", item_cost
        # Using the cost, find the time until we have enough 
        # cookies to buy the item
        time_needed = clicker_state.time_until(item_cost)
        #print "time needed: ", time_needed
        # stop the simulation if we do not have enough
        # time to buy the item
        if (time_needed + clicker_state.get_time() > duration):
            #print time_needed + clicker_state.get_time()
            break
 
        # wait until the time when we can buy the item
        clicker_state.wait(time_needed)
        # buy the item
        clicker_state.buy_item(item, item_cost, 
                              build_info_copy.get_cps(item))
        # update the build information which updates the cost
        # of the item
        build_info_copy.update_item(item)
        
        
    # if time is still left after stopping the simulation
    # allow cookies to accumulate for that amount of time
    if (clicker_state.get_time() < duration):
        clicker_state.wait(duration - clicker_state.get_time())
        
        
    
    return clicker_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    # initalize varialbes
    cheapest_cost = float("inf")
    cheapest_item = None
    # calculate the maximum cookies that can be used to
    # buy an item
    max_cost = cookies + time_left * cps
    # get all the items available to buy
    items_list = build_info.build_items()   
    
    # find the cheapest item that can be afforded
    for item in items_list:
        current_item_cost = build_info.get_cost(item)
        if (current_item_cost <= max_cost 
            and current_item_cost < cheapest_cost):
            cheapest_cost = current_item_cost
            cheapest_item = item
            
    return cheapest_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    # initalize varialbes
    expensive_cost = float("-inf")
    expensive_item = None
    # calculate the maximum cookies that can be used to
    # buy an item    
    max_cost = cookies + time_left * cps
    # get all the items available to buy
    items_list = build_info.build_items()

    # find the most expensive item that can be afforded
    for item in items_list:
        current_item_cost = build_info.get_cost(item)
        if (current_item_cost <= max_cost 
            and current_item_cost > expensive_cost):
            expensive_cost = current_item_cost
            expensive_item = item
            
    return expensive_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    Always picks the item that minimizes the item's 
    cost to item's cps 
    """
    # initalize varialbes
    min_cost_to_cps = float("inf")
    best_item = None
    # calculate the maximum cookies that can be used to
    # buy an item
    max_cost = cookies + time_left * cps
    # get all the items available to buy
    items_list = build_info.build_items()
    
    # buy the item that minimizes the cost per cps
    for item in items_list:
        item_cost = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        item_cost_to_cps = item_cost / item_cps 
        if (item_cost <= max_cost and 
            item_cost_to_cps < min_cost_to_cps):
            min_cost_to_cps = item_cost_to_cps
            best_item = item
    
    return best_item
        
def run_strategy(strategies, time):
    """
    Run a simulation for all strategies for the give time
    
    strategies is a dictionary with key the strategy name
    of type string and value the strategy function name
    """
    # initialize the local variables
    states = []
    histories = []
    plot_history = []
    strategy_names = []

    # store all the states and their names for each strategy
    for strategy_name, strategy_type in strategies.items():
        state =  simulate_clicker(provided.BuildInfo(), 
                                  time, strategy_type)
        states.append(state)
        strategy_names.append(strategy_name)
        print strategy_name, ":", state
        
    # get the history of each strategy's state    
    for state in states:
        histories.append(state.get_history())
        
    # store just the time and total cookies from the history 
    # for plotting purpose
    for history in list(histories):
        history = [(item[0], item[3]) for item in history]
        plot_history.append(history)
        
    # plot all strategies time vs total cookies on one figure    
    simpleplot.plot_lines("strategy plots", 1000, 600, 'Time', 'Total Cookies', 
                          plot_history, True, strategy_names)
    
def run():
    """
    Run the simulator.
    """ 
    
    strategies = {"Cheap":strategy_cheap, 
                  "Expensive": strategy_expensive,
                  "Best": strategy_best}
    
    run_strategy(strategies, SIM_TIME)

#####################################
run the simmulation
#####################################
run()

