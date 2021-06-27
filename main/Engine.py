# Texas Hold Em' for the CLI
# Written by GH on 6-25-2021

# TODO move engine game logic to this file
# TODO refactor game engine to be specific to handling the turn and game startup
import itertools
from random import shuffle
from Winning_Hands_Logic import hand_rank_compare
from Winning_Hands_Logic import card_logic_start
from Card_Deck import cards
from Player import player
 
class engine():
    def __init__(self):
        self.cards_on_table = []
        self.chips_in_pot = 0
        self.min_bets = [10, 20]
        self.dealer = None #clarify what dealer is
        self.player_roster = []
        self.round_roster = []
        self.round_winner = None
        self.round_count = 0
        self.current_dealer = None
        self.previous_dealer = None

    # new npcs based on how many the user wants.
    def npcs_to_play(self):
        while True:
            try:
                num_npcs = int(input("How many NPCs would you like to play against \(1-7\)? "))
                if 1 <= num_npcs <= 7:
                    break
            except:
                print("Please enter a number between 1 and 7")

        for i in range(1, num_npcs+1):
            self.player_roster.append(player("NPC_" + str(i)))

