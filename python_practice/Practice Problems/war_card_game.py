import random

suits = ['Diamonds','Hearts', 'Clovers', 'Spades']
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

player_hand=[]
computer_hand=[]


deck=[]

for suit in suits:
    for rank in ranks:
        deck.append((rank, suit))

#print(deck)
        
random.shuffle(deck)

player_hand = deck[:26]
computer_hand = deck[26:]

# print(len(player_hand))
# print(len(computer_hand))

def compare_cards(player, computer):
    rank_order = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

    player_rank_index = rank_order.index(player[0])
    comp_rank_index = rank_order.index(computer[0])

    if player_rank_index > comp_rank_index:
        return 'Player'
    elif player_rank_index < comp_rank_index:
        return 'Computer'
    else:
        return 'Tie'
    

while len(player_hand) > 0 and len(computer_hand) > 0:
    input("Press Enter to play a round...")

    player = player_hand.pop(0)
    computer = computer_hand.pop(0)

    print(f"Player's Card: {player}")
    print(f"Computer's Card: {computer}")

    winner = compare_cards(player, computer)

    if winner == 'Player':
        print("Player wins the round!")
    elif winner == 'Computer':
        print("Computer wins the round!")

    else:
        print("Tie!")

if len(player_hand) == 0:
    print("Player wins the game!")
elif len(computer_hand) == 0:
    print("Computer wins the game!")