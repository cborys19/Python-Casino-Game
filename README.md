# Python-Casino-Game

1)	Please create a Python program based on the game of craps. The rules of the game are as follows:
* Two dices are required to play and a player rolls two six-sided dice and adds the numbers rolled together.
* If on the first roll a player encounters a total of 7 or 11 the player automatically wins, and if the player rolls a total of 2, 3, or 12 the player automatically loses, and play is over.
* If a player rolls a total of 4, 5, 6, 8, 9, or 10 on their first roll, that number becomes the ‘point. Then the player continues to roll the two dice again until one of two things happens either they roll the ‘point’ again, in which case they win, or they roll a 7, in which case they lose.
* during the rolling of the dice between win or lose, the player(s) can place wagers on:
	4,5,6,8,9 or 10
	Or
	Doubles of
	3’s (pays 9 to 1), 4’s (pays 9 to 1), 5’s (pays 7 to 1) or 2’s (pays 7 to 1)
A. Your program must set the initial dollar value for the person to have 100 coins. They can walk around from the table at any time, so you will need to have them enter a specified sentinel value if they wish to leave. Once they leave, you will display how many coins they have. 
** the person rolling the dice must put 5 coins on the PASS line to begin the game **
B. The user will be allowed to bet before the game begins on the PASS line (betting that the winner Winner) or DON’T PASS line (betting on the player losing). Value from 1 to 5 coins. 
C. After the initial roll and the POINT is set, then the user can place bets from 1 to 5 coins, (if they still have coins) on if the user will roll a specific number before they win or lose. Potential side-bets are:
	* 4
	* 5
	* 6
	* 8
	* 9
	* 10
*** OR 2’s, 3’s, 4’s or 5’s (see above payouts)
D. If the player wins on a side-bet then it automatically adds to their total coins and is removed from the board and increases their overall balance. 
	i.e., If a player makes places 2 coins on the number 4, and the number is rolled before the player makes their point or rolls a CRAPS, then the player receives 4 coins (their 2 coins plus 2 from their bet). 
E. If the shooter rolls a CRAPS (meaning a 7) before the point is made, then all of the side-bets are lost, and you must decrease their overall balance. 
