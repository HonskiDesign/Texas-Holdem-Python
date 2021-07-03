# Texas Hold Em' for the CLI
# Written by GH on 6-25-2021

# TODO move engine game logic to this file
# TODO refactor game engine to be specific to handling the turn and game startup

import itertools
from Player import player
 
class engine():
    def __init__(self):
        self.cards_on_table = []
        self.chips_in_pot = 0
        self.min_bets = [20, 10]
        self.dealer = None #clarify what dealer is
        self.player_roster = []
        self.round_roster = []
        self.round_winner = None
        self.round_count = 0
        self.current_dealer = None
        self.previous_dealer = None

##### Game Setup #####

    # new npcs based on how many the user wants.
    def npcs_to_play(self):
        while True:
            try:
                num_npcs = int(input("How many NPCs would you like to play against (1-7)"))
                if 1 <= num_npcs <= 7:
                    break
            except:
                print("Please enter a number between 1 and 7")

        for i in range(1, num_npcs+1):
            self.player_roster.append(player("NPC"))

    # Get Player
    def get_player(self):
        self.player_roster.append(player())

    
##### Game Loop Methods #####

    # 0. Players participating this round
    def round_start(self):
        print("***** ROUND {} *****".format(self.round_count))
        for player in self.player_roster:
            if player.chips > 0:
                self.round_roster.append(player)

    # 1. Set Dealer
    def set_dealer(self):
        if self.round_count == 0:
            self.current_dealer = self.round_roster[0]
            self.previous_dealer = self.round_roster[-1]
        else:
            self.previous_dealer = self.current_dealer
            # TODO Current Dealer Cycle Function Broken
            self.current_dealer = next(itertools.cycle(self.round_roster))
            print(self.current_dealer.name + " is the Dealer")
        self.current_dealer.is_betting = True
        self.previous_dealer.is_betting = True


    # 2. Get Ante
    def ante_up(self):
        self.current_dealer.chips -= self.min_bets[0]
        self.chips_in_pot += self.min_bets[0]
        self.previous_dealer.chips -= self.min_bets[1]
        self.chips_in_pot += self.min_bets[1]

    # 3. Get Initial Bets Pre-Deal
    # 4. Deal - Handled by Game_Deck
    # 5. Get More bets, check folds, check winner?
    # 6. Flop
    # 7. Get more bets, check folds, check winner?
    # 8. Turn
    # 9. Get more bets, check folds, check winner?
    # 10. River
    # 11. Get more bets, check folds
    # 12. Showdown.
    # 13. End Round
    def end_of_round(self):
        
        ## Find Winner, give chips
        # TODO need to figure out how to divy pot
        #print(self.round_winner.name + " has won the round and $" + self.chips_in_pot + "!")
        #self.round_winner.chips += self.chips_in_pot
        #self.chips_in_pot = 0

        ## Remove players no longer able to bet
        for player in self.round_roster:
            if player.chips == 0:
                print(f"{player.name} has been eliminated!")
                self.round_roster.remove(player)
        
        ## Update minimum bet amounds by a factor of 2 every 5 rounds of play
        self.round_count += 1
        if self.round_count % 5 == 0:
            for i in range(len(self.min_bets)):
                self.min_bets[i] *= 2
       
        ans = input('Hit Enter to conitinue or Q to quit: ')
        if ans.lower() == 'q':
            quit()


# TODO need way to manage game state or progress in steps.

##### DEBUG #####
#game = engine()

