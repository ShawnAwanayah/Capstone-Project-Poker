Program to simulate a game of poker.


Everytime a new game runs, the program will ask you if you want to play.
If you have played 1 or more games then it will show you your win percentage along with you total number of wins and games played.
The game is played with you (you are called "user") and 3 other players all starting with £100.
Each game the order in which the player's take turns is shuffled.


The game will show the original deck which is two cards, every card is in the format (suit,value) with multiple cards being [(suit1,value1),(suit2,value2)...], and each turn will give you the option to see your cards,
raise, call the last bet or fold; unless you are 1st to play in which the game takes £5 from you and adds to the pot then got to the next person.


If you choose to "see cards", then it will show you your cards and the the same 4 options will come up again.


If you choose to "call", then it will take whatever the last bet was from your money and add it to the pot.


If you choose to "raise", then it will ask you how much you want to raise by and this will take away the last bet + raise from your money.


If you choose to fold then it will remove you from the game.


The other 4 players will randomly call or raise (they will always raise by 10 if they do) however, they do not have the option to fold.


The amount of money in the pot and the last bet is printed after everyone's turn.


Turns will keep happening until there are 5 cards in the deck, when this happens it will check everyone's hand to see who has the best
see https://boardgamegeek.com/boardgame/1115/poker for the best possible hands (five of a kind is excluded and the royal flush is not differentiated from a straight flush)

Afterwards it will print the winner/winners, what hand they won with and how much of the pot they won.
