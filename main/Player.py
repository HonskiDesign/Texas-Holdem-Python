# Texas Hold Em' for the CLI

## Player Class Object

class player:
    current_npcs = 0
    def __init__(self, player_type=None):
        self.player_type = player_type
        self.name = self.get_name()
        self.chips = 10000
        self.hand = []
        self.hand_rank = []
        self.is_playing = True
        self.is_betting = False
    
    ## Methods to get Player names and name NPCs
    def npc_name(self):
        player.current_npcs += 1
        name = "NPC_" + str(player.current_npcs)
        return name

    def get_name(self):
        if self.player_type is None:
            self.player_type = 'Human'
            player_name = input("Now what's your name, my friend?\n> ")
            return player_name
        else:
            return self.npc_name()
 
