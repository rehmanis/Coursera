# Mini-project #4 Fifteen Puzzles

Developed the logic to solve the Fifteen Puzzles game in CodeSkulptor, a browser-based Python interpreter, as part of the coursework. To see the solver in action, go [here](http://www.codeskulptor.org/#user46_p9CLHFUXsW_56.py) and press the play button on the top left corner. A window will pop up, with the unshuffled puzzle. Use arrow key to shuffle the puzzle as desired and then press the Solve button to visually solve the puzzle.

Link to my test suite for the implementation:
<http://www.codeskulptor.org/#user46_ZoVa3j3l3k_66.py>

Mini-project overview taken from course page can be found below:
* This week's homework introduced you to the Fifteen puzzle and outlined the highlights of building a solver for the puzzle. As described in the homework, the solution process for a puzzle of size <a href="https://www.codecogs.com/eqnedit.php?latex=m&space;\times&space;n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m&space;\times&space;n" title="m \times n" /></a> has three phases:

1. Solve the bottom m-2 rows of the puzzle in a row by row manner from bottom to top. Each individual row will be solved in a right to left order.
2. Solve the rightmost n-2 columns of the top two rows of the puzzle (in a right to left order). Each column consists of two unsolved positions and will be solved in a bottom to top order.
3. Solve the upper left <a href="https://www.codecogs.com/eqnedit.php?latex=2&space;\times&space;2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2&space;\times&space;2" title="2 \times 2" /></a> portion of the puzzle directly.

Complete project description can be found at : 
<https://www.coursera.org/learn/principles-of-computing-2/supplement/08FqM/mini-project-description>
