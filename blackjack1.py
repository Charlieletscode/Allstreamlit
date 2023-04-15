import streamlit as st
import random

# Define the card deck
CARD_DECK = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
CARD_VALUES = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

# Define a function to calculate the value of a hand
def calculate_hand(hand):
    total = 0
    for card in hand:
        total += CARD_VALUES[card]
    # If the hand contains an Ace and the total is over 21, count the Ace as 1 instead of 11
    for card in hand:
        if card == 'Ace' and total > 21:
            total -= 10
    return total

# Define a function to deal a new hand
def deal_hand():
    deck = CARD_DECK * 4
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return deck, player_hand, dealer_hand

# Define the Streamlit app
def main():
    st.set_page_config(page_title="Blackjack", page_icon=":spades:", layout="wide")
    st.title("Blackjack")
    st.write("Welcome to the Blackjack game!")
    
    # Start the game
    game_over = False
    start_game = st.button("New Hand")
    if start_game:
        deck, player_hand, dealer_hand = deal_hand()
        player_score = calculate_hand(player_hand)
        dealer_score = calculate_hand(dealer_hand)
        
        # Show the player's hand and the dealer's first card
        st.write("**Your hand:**", player_hand, "(", player_score, ")")
        st.write("**Dealer's hand:**", [dealer_hand[0], 'X'])
        
        # Check if the player gets a Blackjack
        if player_score == 21:
            st.write("Blackjack! You win!")
            game_over = True
        
        # Let the player hit or stand
        while not game_over:
            hit_button = st.button("Hit")
            stand_button = st.button("Stand")
            if hit_button:
                player_hand.append(deck.pop())
                player_score = calculate_hand(player_hand)
                st.write("**Your hand:**", player_hand, "(", player_score, ")")
                st.write("**Dealer's hand:**", [dealer_hand[0], 'X'])

                # Check if the player busts
                if player_score > 21:
                    st.write("Bust! You lose!")
                    game_over = True

            elif stand_button:
                while calculate_hand(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
                dealer_score = calculate_hand(dealer_hand)
                st.write("**Your hand:**", player_hand, "(", player_score, ")")
                st.write("**Dealer's hand:**", dealer_hand, "(", dealer_score, ")")

                # Check if the dealer busts
                if dealer_score > 21:
                    st.write("Dealer bust! You win!")
                    game_over = True

                # Check who wins
                elif player_score > dealer_score:
                    st.write("You win!")
                    game_over = True
                elif player_score < dealer_score:
                    st.write("You lose!")
                    game_over = True
                else:
                    st.warning("It's a tie!")
                    game_over = True


if __name__ == '__main__':
    main()