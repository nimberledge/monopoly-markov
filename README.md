# monopoly-markov
Using Markov Chains to a play a simplified version of monopoly.

**Rules to implement:**

&nbsp;
The monopoly board in picture represents a simplified version of the monopoly game. Strategy for monopoly can often be complicated, but a good place to begin strategizing is to find out which squares are most frequently visited. Players begin the game on the Go (0) square, rolling a dice to determine how many places forward they move.

For example, on the first throw of the dice, if a player rolls 2, they go to the square (0 + 2) = 2, and land in Grainger Library. If a player happens to roll a 6, their turn continues and includes one more dice roll. They will move to the slot that is the sum of the two previous dice rolls, for example if they roll a 6 on the first turn and then a 3 on the extra dice roll, the player will land up at (6 + 3 = 9) the 9th square, or UGL. If a player rolls 2 6s in a row, they move 12 steps forward (i.e. the second 6 does not cause a re-roll). Note that it is impossible to go from the 0 index to the 6 index in a single turn.

There are also certain spots on the board that change the movement mechanics. Index 12 says "go to jail", and moves a player to the jail index without exception. Indices 3, 7, and 14 are chance cards. In the original game, players would draw from a pile of cards that allow certain actions. The only action relevant to the movement mechanics is "pass go", which moves a player to the 0 index for the start of their next turn. Players will pick up a "pass go" card with a probability of 1 in 5 (0.2).

Assuming that dice rolls are purely random, model the movement in the game to find the most visited squares on the board.
