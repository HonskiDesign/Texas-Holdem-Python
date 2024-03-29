# Texas Hold Em' for the CLI
# Winning Hand Algo

# Written by GH on 2-3-2020


# This is the start of all logic. Poker_Main.py is passing the
# deck and hand to this function

def card_logic_start(hand, table):
    ## There are rankings for hands and ranking for cards(for hand ties)
    card_rankings = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    hand_rankings = {'HC':0, 'PR':1, '2P':2, '3K':3, 'ST':4, 'FL':5, 'FH':6, '4K':7, 'SF':8, 'RF':9}

    # Get all the cards together
    all_cards = hand + table

    # Sort the cards by value
    all_cards.sort(key=lambda x: card_rankings.index(x[0]), reverse=True)
    
    print(all_cards) #for debugging

    # Set hand rank to 0
    hand_rank = [0,0,0,0,0]
    winning_hand = []

    # Create list of values and suits
    value_list = []
    suit_list = []
    for card in all_cards:
        value_list.append(card[0])
        suit_list.append(card[1])


    # Check for Straight Flush

    # Check for Straight

    # Check for Full House

    # Check for Flush
    for suit in set(suit_list):
        if suit_list.count(suit) == 5 and hand_rank[0] < int(hand_rankings['FL']):
            hand_rank[0] = hand_rankings['FL']
            for card in all_cards:
                if card[1] == suit and len(winning_hand) < 5:
                    winning_hand.append(card)
        else:
            continue

    # Check for pairs, three of kind, four of kind
    for kind in set(value_list):
        if value_list.count(kind) == 4 and hand_rank[0] < int(hand_rankings['4K']):
            hand_rank[0] = hand_rankings['4K']
            for card in all_cards:
                if card[0] == kind:
                    winning_hand.append(card)
                    all_cards.pop(card)
        if value_list.count(kind) == 3 and hand_rank[0] < int(hand_rankings['3K']):
            hand_rank[0] = hand_rankings['3K']
        if value_list.count(kind) == 2 and hand_rank[0] < int(hand_rankings['PR']):
            hand_rank[0] = hand_rankings['PR']
        if value_list.count(kind) == 2 and hand_rank[0] == int(hand_rankings['PR']):
            hand_rank[0] == int(hand_rankings['2P'])     
        elif len(winning_hand) < 5:
            winning_hand.append(all_cards.pop(0))

    
    
    print("Player's Hand: ", winning_hand)
    return hand_rank

# This function is to compare hands fo remaining players to decide winner.
def hand_rank_compare(playerRoster):
    winning_player = playerRoster[0]
    for player in playerRoster[1:]:
        temp_player = player
        for x in range(5):
            if temp_player.hand_rank[x] > winning_player.hand_rank[x]:
                winning_player = temp_player
                break
            else:
                continue     
    return winning_player

