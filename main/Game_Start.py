# Texas Hold'em for the CLI
# Written by GH on 6-27-2021

from Engine import engine

# Welcome Screen
print("Welcome to Texas Hold'em")

# Game Initialize
game = engine()
game.get_player()
game.npcs_to_play()

# Call Game Loop
while True:
    game.round_start()
    game.set_dealer()
    print(f"Min bets are {game.min_bets[0]} & {game.min_bets[1]}")
    game.ante_up()

    for player in game.player_roster:
        print("---Player---")
        print(player.name)
        print(player.chips)
        print(player.hand)
        print(player.is_betting)

    game.end_of_round()
# Match End

