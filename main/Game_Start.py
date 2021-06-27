# Texas Hold'em for the CLI
# Written by GH on 6-27-2021

from Engine import engine

# Welcome Screen
print("Welcome to Texas Hold'em")

# Game Initialize
game = engine()
game.get_player()
game.npcs_to_play()
game.round_start()
game.set_dealer()

# Call Game Loop

# Match End

# TODO remove this section once game is working
## DEBUG ##
for player in game.player_roster:
    print("---Player---")
    print(player.name)
    print(player.chips)
    print(player.hand)
    print(player.is_betting)
