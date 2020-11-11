# Texas Hold Em' for the CLI
# Written by GH on 2-3-2020

import itertools
from random import shuffle
from Winning_Hands_Logic import hand_rank_compare
from Winning_Hands_Logic import card_logic_start
from Card_Deck import cards
 #import NPC_Logic - not currently used

#***************#

## Player Class Object

class player:
    current_npcs = 0
    def __init__(self, player_type=None):
        self.player_type = player_type
        self.name = self.get_name()
        self.chips = 10000
        self.hand = list()
        self.hand_rank = []
        self.is_betting = False
    
    ## Methods to get Player names and name NPCs
    def npc_name(self):
        player.current_npcs += 1
        name = "NPC_" + str(player.current_npcs)
        return name

    def get_name(self):
        if self.player_type is None:
            player_name = input("Now what's your name, my friend?\n> ")
            return player_name
        else:
            return self.npc_name()
    
    def bet(self):
        pass
    
#***************#

## Game Engine Class Object

class engine():
    def __init__(self):
        self.cards_on_table = []
        self.chips_in_pot = 0
        self.min_bets = [10, 20]
        self.dealer = None
        self.player_roster = []
        self.round_roster = []
        self.round_winner = None
        self.round_count = 0
        self.current_dealer = None
        self.previous_dealer = None


    ## Simple intro to the game
    def game_start(self):
        print("\n" * 5)
        print("Welcome to Honski's Texas Hold'em!")
        print("How bout we start a game!")
    
    def round_start(self):
        for player in self.player_roster:
            self.round_roster.append(player)

    ## Need to write function to decide how many NPCs are to play
    def npcs_to_play(self):
        pass

    ## Creating Players and adding them to the roster

    def get_players(self):
        
        pass

    # Need To Write function to set the dealer token
    def set_dealer(self):
        self.previous_dealer = self.current_dealer
        self.current_dealer = next(itertools.cycle(self.player_roster))

    ## This will promp the player for a bet and add the bet to the pot.
    def bet(self):
        print(f"Please make a bet. The minimum bet is {self.min_bets[1]}!")
        chips_to_bet = int(input("> "))
        if chips_to_bet < self.min_bets[1]:
            print(f"You did not make the minimum bet of {self.min_bets[1]}!")
            self.bet()
        else:
            self.chips_in_pot = chips_to_bet
    
    ## Need a function for the bot to bet
    def npc_bet(self):
        pass

    ## Deals the players listed in the player roster their cards
    def deal_players(self):
        for player in self.player_roster:
            player.hand = game_deck.deal(2)

    ## Deals the the flop
    def the_flop(self):
        game_deck.burn()
        self.cards_on_table = game_deck.deal(3)

    ## Deals the turn card
    def the_turn(self):
        game_deck.burn()
        self.cards_on_table = self.cards_on_table + game_deck.deal(1)

    # Deals the river card
    def the_river(self):
        game_deck.burn()
        self.cards_on_table = self.cards_on_table + game_deck.deal(1)

    # Folds hand of player
    def fold(self, player):
        player.hand.clear()

    # End of round actions, deciding winner, adjusting chips, removing players with no chips, etc.
    def end_of_round(self):
        
        ## Find Winner, give chips
        self.round_winner = None

        ## Remove players no longer able to bet
        for player in player_roster:
            if player.chips == 0:
                print(f"{player.name} has been eliminated!")
                player_roster.remove(player)
        
        ## Update minimum bet amounds by a factor of 2 every 5 rounds of play
        self.round_count += 1
        if self.round_count % 5 == 0:
            for i in range(len(self.min_bets)):
                self.min_bets[i] *= 2


#***************#

## Game Initialize
game_main = engine()
game_main.game_start()
game_main.player_roster = []

## Create the Game Deck and shuffle it.
game_deck = cards()
game_deck.shuff()

## Create and add Players to roster
Player1 = player()
game_main.player_roster.append(Player1)
npc_1 = player("NPC")
game_main.player_roster.append(npc_1)
npc_2 = player("NPC")
game_main.player_roster.append(npc_2)


#***************#

## Main Game Start - Need to make this into a loop.n

# Set Dealer
game_main.set_dealer()


## Deal Cards - 
game_main.deal_players()


## Anything below here is just code to test

print('-' * 10)



game_main.the_flop()
game_main.the_turn()
game_main.the_river()

for player in game_main.player_roster:
    print(player.name)
    print(player.hand)
    player.hand_rank = card_logic_start(player.hand, game_main.cards_on_table)
    print(player.hand_rank)

print('\n')
print("The Winner is " + hand_rank_compare(game_main.player_roster).name + '!')

