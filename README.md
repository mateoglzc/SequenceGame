# Sequence Game

This is a biginner Sequence game made in Python using the Pygame library. It's not a super clean code or a super optimized ( it's probably the contrary of that ) but
I'm all about learning so feel free to send fixes and optimizations.

##  How to play
Here's a quick tutorial of how this game works:

* First of all it requieres two players.
* At the start of the game each player is given three cards that are represented by dots located on the botton and left side. 
* The bottom side dots ( cards ) belong to Player 1 and the left side dots ( cards ) belong to Player 2.
* Starting with Player 1 each player will click on a color in the board that corresponds to one color that they have in their cards.
* Each time you click on a color that corresponds with a card that you have you would have "used" that card and a new one would be given to you. ( There's a bug in this step )
* The corners of the board are free spaces and do not require the use of a card.
* A player wins when they are the first to make a line of four. It can be a vertical, horizontal or diagonal line.

There's some bugs that i have found but have no clue how to solve them, if you come across another bug or know how to fix some make sure to send your fix or discovery.

##### Bugs found
###### * When placing a chip on a square it may not change the card that you use to place that chip. This happens because cards are given by location not by color. 
