# Mini-project #1 - Rock-paper-scissors-lizard-Spock

Implemented the another version of the classic rock-paper-scissors game in CodeSkulptor, a browser-based Python interpreter, as part of the coursework. To play the game go [here](http://www.codeskulptor.org/#user46_xghMO1JnR7_2.py) and press the play button on the top left corner. A call to each of the five options--rock, paper, scissors, lizard, Spock, has already added in the code and the computer's choice is then randomly chosen with the result of the game printed on the console on the right. Rules for the modified version of rock-paper-scissors game can be found below in the mini-project overview:

Mini-project overview taken from course page can be found below:
* Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. Each choice wins against two other choices, loses against two other choices and ties against itself. Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory". The Wikipedia entry for RPSLS gives the complete description of the details of the game.

* In our first mini-project, we will build a Python function rpsls(name) that takes as input the string name, which is one of "rock", "paper", "scissors", "lizard", or "Spock". The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by generating its own random choice from these alternatives and then determining the winner using a simple rule that we will next describe.

* "While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically determine who wins a round of RPSLS, coding up these rules would require a large number (5x5=25) of if/elif/else clauses in your mini-project code. A simpler method for determining the winner is to assign each of the five choices a number:
	* 0 — rock
	* 1 — Spock
	* 2 — paper
	* 3 — lizard
	* 4 — scissors

* In this expanded list, each choice wins against the preceding two choices and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).

Complete Mini-Project Description can be found at: 
<https://www.coursera.org/learn/interactive-python-1/supplement/ijRP5/mini-project-description>


