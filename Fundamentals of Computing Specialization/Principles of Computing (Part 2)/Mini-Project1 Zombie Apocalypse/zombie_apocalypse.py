"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        # clear all grid cell to be passable i.e. cell that
        # are EMPTY
        poc_grid.Grid.clear(self)
        # reinitialize the human and zombie lists to
        # be empty
        self._human_list = []
        self._zombie_list = []
        
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie
            

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # store the height and width of the grid
        height = poc_grid.Grid.get_grid_height(self)
        width = poc_grid.Grid.get_grid_width(self)
        # create a grid that tracks the visited cells of the grid
        # and intialize all locations to be EMPTY i.e. not visited
        visited = [[EMPTY for dummy_col in range(width)] 
                       for dummy_row in range(height)]
        
        # create a distance field to keep track of the shortest
        # distance from a entity type and initialize it as height*width
        # since the distance larger than any possible distance
        distance_field = [[height * width for dummy_col in range(width)] 
                       for dummy_row in range(height)]
        
        # create a queue for breath first search
        boundary = poc_queue.Queue()
        # map the respective entity type to its generator function
        map_entity_type = {HUMAN: self.humans, ZOMBIE: self.zombies}
        # add all human or zombie locations to the queue 
        # and mark those locations as visited and the
        # distance at that location as zero
        for row, col in map_entity_type[entity_type]():
            boundary.enqueue((row, col))
            visited[row][col] = FULL
            distance_field[row][col] = 0
        # begin the breath first search
        while(len(boundary) > 0 ):
            # get the current cell i.e the grid location
            # of the zombie/human
            current_cell = boundary.dequeue()
            # get all of the current cells four neighbours and iterate
            # over them
            for neighbor_cell in poc_grid.Grid.four_neighbors(self, 
                                                              current_cell[0], 
                                                              current_cell[1]):
                # if neigboring cell is passable and has not yet been visited
                # add it to the queue for BFS, mark it as visited and 
                # update the distance. 
                if (poc_grid.Grid.is_empty(self, neighbor_cell[0], neighbor_cell[1]) 
                    and visited[neighbor_cell[0]][neighbor_cell[1]] == EMPTY):
                    boundary.enqueue(neighbor_cell)
                    visited[neighbor_cell[0]][neighbor_cell[1]] = FULL
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = (
                        distance_field[current_cell[0]][current_cell[1]] + 1)
                                                                                         
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        # initialize the list that stores the new location of the 
        # humans after each step of the simulation
        new_human_locs = []
        # iterate over all human locations using it's generator
        for human in self.humans():
            # initialize the maximum distance that the human
            # can travel after each step of simulation as
            # the current human location
            max_dis = zombie_distance_field[human[0]][human[1]]
            # store the location of this distance that maximizes
            # its location from the nearest zombie
            safest_loc = human
            # get all 8 neighboring cell of this current human 
            neighbors = poc_grid.Grid.eight_neighbors(self, 
                                                      human[0], human[1])
            # iterate over all neigboring cells to find which 
            # neigboring cell maximizes the current human's
            # distance from the nearest zombie
            for neighbor in neighbors:
                if (poc_grid.Grid.is_empty(self, 
                                           neighbor[0], 
                                           neighbor[1]) 
                    and zombie_distance_field[neighbor[0]][neighbor[1]] > max_dis):
                    max_dis = zombie_distance_field[neighbor[0]][neighbor[1]]
                    safest_loc = neighbor
            
            # store this location that maximizes current human's
            # distance from the nearest zombie
            new_human_locs += [safest_loc]
        # update the existing human locations list with the new humans
        # locations found earlier
        self._human_list = new_human_locs

             
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        # initialize the list that stores the new location of the 
        # zombie after each step of the simulation        
        new_zombie_locs = []
        # iterate over all zombie locations using it's generator        
        for zombie in self.zombies():
            # initialize the current zombie location as the 
            # location that minimizes its distance from nearest
            # human
            best_loc = zombie
            # intialize the current zombie location's distance
            # on the human distance field as the minimum distance.
            # This location becomes nearest location to human
            # if no neigbhoring cells are smaller than this distance
            min_dis = human_distance_field[zombie[0]][zombie[1]]
            # get all the neigboring cells of the current zombie
            neighbors = poc_grid.Grid.four_neighbors(self, 
                                                      zombie[0], zombie[1])
            # iterate over all neigboring cells to find which 
            # neigboring cell minimize the current zombie's
            # distance from the nearest human
            for neighbor in neighbors:
                if (poc_grid.Grid.is_empty(self, 
                                           neighbor[0], 
                                           neighbor[1]) 
                    and human_distance_field[neighbor[0]][neighbor[1]] < min_dis):
                    min_dis = human_distance_field[neighbor[0]][neighbor[1]]
                    best_loc = neighbor
                    
            # store this location that minimizes current zombie's
            # distance from the nearest human. 
            new_zombie_locs += [best_loc]

        self._zombie_list = new_zombie_locs


# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))



