# Mini-project #4 - Yahtzee

Implemented the game strategy logic for a simplified version of the game Yahtzee in CodeSkulptor, a browser-based Python interpreter, as part of the coursework. 

Link to my solution:
<http://www.codeskulptor.org/#user46_a5e527xGfZ_58.py>

Link to the test suite for my solution: 
<http://www.codeskulptor.org/#user46_i4ScIuelhi_93.py>

Mini-project overview taken from course page can be found below:
*[Yahtzee](https://en.wikipedia.org/wiki/Yahtzee) is a dice game played with 5 dice where you try to score the most points by matching certain combinations. You can play the game [here](https://cardgames.io/yahtzee/). In Yahtzee, you get to roll the dice three times on each turn. After the first roll, you may hold as many dice as you would like and roll the remaining free dice. After this second roll, you may again hold as many dice as you would like and roll the rest. Once you stop (either because you have exhausted your three rolls or you are satisfied with the dice you have), you score the dice in one box on the score card.

* For this mini-project, we will implement a strategy function designed to help you choose which dice to hold after your second roll during the first turn of a game of Yahtzee. This function will consider all possible choices of dice to hold and recommend the choice that maximizes the expected value of your score after the final roll.

* To simplify the mini-project, we will only consider scores corresponding to the "upper" section of the scorecard. Boxes in the upper section correspond to numbers on the dice. After each turn, you may choose one empty box and enter the sum of the dice you have with the corresponding number. For example, if you rolled **(2, 3, 3, 3, 4)**, you could score **2** in the Twos box, **9** in the Threes box, or **4** in the Fours box. (Restricting scoring to the upper section will also allow you to debug/test your strategy function on smaller numbers of dice.)


Complete project description can be found at : 
<https://www.coursera.org/learn/principles-of-computing-1/supplement/MWNxX/mini-project-description>


