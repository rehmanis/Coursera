# Mini-project #1 Zombie Apocalypse

Overview
* In this mini-project, we will create a simulation of zombies and humans interacting on a grid. As in the movies, our zombies are hungry for human brains. As a result, zombies chase humans and humans flee from zombies. To keep our simulation manageable, the positions of the zombies and humans will be restricted to a grid. In our simulation, zombies are not very agile and can only move up, down, left or right in one step of the simulation. On the other hand, humans are more agile and can move in these four directions as well as the four neighboring diagonal directions. If a zombie catches a human by positioning itself in the same cell, the zombie enjoys some delicious human brains. Being a Computer Scientist, the human has plenty of brains to spare and continues to live on in our simulation.

* To enhance the realism of our simulation, some of the cells in this grid will be marked as impassable and restrict zombie/human movement so that they can not move through these cells. Our task in this simulation is to implement an **Apocalypse** class that encapsulates the core mechanisms of this simulation and that interacts with a GUI that we have created for visualizing the simulation in CodeSkulptor. This **Apocalypse** class is a sub-class of the **Grid** class and inherits the **Grid** class methods. Passable cells in the grid correspond to **EMPTY** cells while **FULL** cells are impassable. Humans and zombies can only inhabit passable cells of the grid. However, several humans and zombies may inhabit the same grid cell.

* This **Apocalypse** class also includes two lists, one for zombies and one for humans. Note that the entries in each list are cell indices of the form **(row,col)** that represent the position of zombies/humans in the grid. Each step in the simulation will either update the positions of the zombies based on the state of the grid and the position of the humans or update the positions of the humans based on the state of the grid and the position of the zombies.

Complete project decription can be found at : 
<https://www.coursera.org/learn/principles-of-computing-2/supplement/3VwCE/mini-project-description>

Link to my solution: <http://www.codeskulptor.org/#user46_uQfN1iv6Qq_0.py>