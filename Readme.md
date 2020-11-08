# Texas Hold'em

#### A command line Texas Hold'em game
This project is a way for me to learn basic programming skills in python whilst utilizing multiple other skills such as using Git, working from the Linux CLI, and editing with VIM. While the majority of the code was originally written in VS Code, the effects of the pandemic pushed me away from practice. I have since pickup practicing again, but have taken a new route learning Linux using WSL and VIM.

#### Directory structure

```
texas_holdem/
    main/
		__init__.py
		Poker_Main.py
		Winning_Hands_Logic.py
		Card_Deck.py
		NPC_Logic.py
    bin/
    docs/
    setup.py
    tests/
	TexasHoldem_tests.py
	__init__.py
```

### Poker_Main.py
This file is where you execute the game from.

### Winning_Hands_Logic.py
This file contains the algorithms for deciding which player has the winning hand. I came up with a ranking system for hands and store the rank in a 5 element array. The 7 cards(2 in hand and 5 on the table) are then analysed for the highest possible hand rank combinations. As these are found, they are added to a return list called winning hand.

The first element of the array, address 0, contains the majority rank. This means if the player has a high card and no other card combinations to make a pair or above, the majority rank is set to 0. If the player were to have a pair, the majority rank would then be set to 1. For two-pair, the majority rank would be set to 2. Etc.

The remaining elements in the array will be based on the next card's face value from highest to lowest. So, for a 2 pair combinations, the higher pair's card value will be put in the rank array at address 1 and the majority rank of 2 will be stored in address 0. Then next pair's card value will be put in address 2 and 3. The remaining highest card value will be placed in address 4. Thus, a hand with a 4h, 4s, 3d, 3s, kh, would be ranked as [2,4,3,3,13].
