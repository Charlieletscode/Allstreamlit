import streamlit as st
import random
from PIL import Image
from io import BytesIO

card_images = {}

# Define the card deck
suits = ['hearts', 'diamonds', 'clubs', 'spades']
card_deck = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
card_values = {'ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10}

for suit in suits:
    for rank in card_deck:
        filename = f'source/images/{rank}_of_{suit}.png'
        with open(filename, 'rb') as f:
            img = Image.open(BytesIO(f.read()))
            card_images[(rank, suit)] = img

filename = f'source/images/download.png'
with open(filename, 'rb') as f:
    img = Image.open(BytesIO(f.read()))
    sp = img

# Define a function to calculate the value of a hand
def calculate_hand(hand):
    total = 0
    for card in hand:
        total += card_values[card[0]]
    # If the hand contains an Ace and the total is over 21, count the Ace as 1 instead of 11
    for card in hand:
        if card[0] == 'ace' and total > 21:
            total -= 10
    return total

# Define a function to deal a new hand
def deal_hand():
    deck = []
    for suit in suits:
        for rank in card_deck:
            deck.append((rank, suit))
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return deck, player_hand, dealer_hand

def printcard(st, card_images):
    hand = str(st.session_state.player_cards[0])+" , "+str(st.session_state.player_cards[1])
    dhand = str(st.session_state.dealer_cards[0])+" , "+str(st.session_state.dealer_cards[1])
    col1, col2, col3, col4, col5, col6= st.columns([1,1,1,1,1,4])
    # origin two card + to 5 
    with col1: 
        st.image(card_images[(st.session_state.player_cards[0][0], st.session_state.player_cards[0][1])].resize((125, 181)))
    with col2: 
        st.image(card_images[(st.session_state.player_cards[1][0], st.session_state.player_cards[1][1])].resize((125, 181)))
    if(len(st.session_state.player_cards)==3):
        hand += " , " + str(st.session_state.player_cards[2])
        with col3: 
            st.image(card_images[(st.session_state.player_cards[2][0], st.session_state.player_cards[2][1])].resize((125, 181)))
    if(len(st.session_state.player_cards)==4):
        hand += " , " + str(st.session_state.player_cards[3])
        with col3: 
            st.image(card_images[(st.session_state.player_cards[2][0], st.session_state.player_cards[2][1])].resize((125, 181)))
        with col4: 
            st.image(card_images[(st.session_state.player_cards[3][0], st.session_state.player_cards[3][1])].resize((125, 181)))
    if(len(st.session_state.player_cards)==5):
        hand += " , " + str(st.session_state.player_cards[4])
        with col3: 
            st.image(card_images[(st.session_state.player_cards[2][0], st.session_state.player_cards[2][1])].resize((125, 181)))
        with col4: 
            st.image(card_images[(st.session_state.player_cards[3][0], st.session_state.player_cards[3][1])].resize((125, 181)))
        with col5: 
            st.image(card_images[(st.session_state.player_cards[4][0], st.session_state.player_cards[4][1])].resize((125, 181)))
    st.write("**Your hand:**",  hand,"(", st.session_state.player_score, ")")
    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,4])

    with col1: 
        st.image(card_images[(st.session_state.dealer_cards[0][0], st.session_state.player_cards[0][1])].resize((125, 181)))
    with col2: 
        st.image(card_images[(st.session_state.dealer_cards[1][0], st.session_state.player_cards[1][1])].resize((125, 181)))
    if(len(st.session_state.dealer_cards)==3):
        dhand += " , " + str(st.session_state.dealer_cards[2])
        with col3: 
            st.image(card_images[(st.session_state.dealer_cards[2][0], st.session_state.dealer_cards[2][1])].resize((125, 181)))
    if(len(st.session_state.dealer_cards)==4):
        dhand += " , " + str(st.session_state.dealer_cards[3])
        with col3: 
            st.image(card_images[(st.session_state.dealer_cards[2][0], st.session_state.dealer_cards[2][1])].resize((125, 181)))
        with col4: 
            st.image(card_images[(st.session_state.dealer_cards[3][0], st.session_state.dealer_cards[3][1])].resize((125, 181)))
    if(len(st.session_state.dealer_cards)==5):
        dhand += " , " + str(st.session_state.dealer_cards[4])
        with col3: 
            st.image(card_images[(st.session_state.dealer_cards[2][0], st.session_state.dealer_cards[2][1])].resize((125, 181)))
        with col4: 
            st.image(card_images[(st.session_state.dealer_cards[3][0], st.session_state.dealer_cards[3][1])].resize((125, 181)))
        with col5: 
            st.image(card_images[(st.session_state.dealer_cards[4][0], st.session_state.dealer_cards[4][1])].resize((125, 181)))

    st.write("**Dealer's hand:**", dhand,"(", st.session_state.dealer_score, ")")


st.set_page_config(page_title="Blackjack", page_icon=":spades:", layout="wide")
st.title("Welcome to the Blackjack game!")

# imgBg = cv2.imread('source/images/background.png')

# for rank in card_deck:
#     for suit in suits:
#         st.image(card_images[(rank, suit)].resize((125, 181)))


# st.session_state.game_start = st.button("New Hand")
# # Start the game
# initialize all state
if("game_start" not in st.session_state):
    st.session_state.game_start = False
if("Hit" not in st.session_state):
    st.session_state.Hit = False
if("Stand" not in st.session_state):
    st.session_state.Stand = False
if("deck" not in st.session_state):
    st.session_state.deck = False
if("player_hand" not in st.session_state):
    st.session_state.player_hand = False
if("dealer_hand" not in st.session_state):
    st.session_state.dealer_hand = False
if("player_cards" not in st.session_state):
    st.session_state.player_cards = False
if("dealer_cards" not in st.session_state):
    st.session_state.dealer_cards = False
if("player_score" not in st.session_state):
    st.session_state.player_score = False
if("dealer_score" not in st.session_state):
    st.session_state.dealer_score = False
if("game_over" not in st.session_state):
    st.session_state.game_over = False

def callback():
    st.session_state.game_start = True
def callbackHit():
    st.session_state.Hit = True
def callbackStand():
    st.session_state.Stand = True

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.session_state.game_start = st.button("New Hand", on_click=callback)
with col2:
    st.session_state.Hit = st.button("Hit", on_click=callback)
with col3:
    st.session_state.Stand = st.button("Stand", on_click=callback)
placeholder = st.empty()

with placeholder.container():
    if st.session_state.game_start:
        st.session_state.deck, st.session_state.player_hand, st.session_state.dealer_hand = deal_hand()
        st.session_state.player_cards = st.session_state.player_hand
        st.session_state.dealer_cards = st.session_state.dealer_hand
        st.session_state.player_score = calculate_hand(st.session_state.player_hand)
        st.session_state.dealer_score = calculate_hand(st.session_state.dealer_hand)
        st.session_state.game_over = False
        
        if len(st.session_state.player_cards) <= 2:
            col1, col2, col3 = st.columns([1,1,7])
            with col1: 
                st.image(card_images[(st.session_state.player_cards[0][0], st.session_state.player_cards[0][1])].resize((125, 181)))
            with col2: 
                st.image(card_images[(st.session_state.player_cards[1][0], st.session_state.player_cards[1][1])].resize((125, 181)))
            st.write("**Your hand:**", str(st.session_state.player_cards[0]), " , ", str(st.session_state.player_cards[1]) , "(", st.session_state.player_score, ")")
            col1, col2, col3 = st.columns([1,1,7])
            with col1: 
                st.image(card_images[(st.session_state.dealer_cards[0][0], st.session_state.player_cards[0][1])].resize((125, 181)))
            with col2: 
                st.image(sp.resize((125, 181)))
            st.write("**Dealer's hand:**", str(st.session_state.dealer_cards[0]), " , X")

        if st.session_state.player_score == 21:
            st.session_state.player_score = calculate_hand(st.session_state.player_cards)
            st.empty()
            st.success("Blackjack! You win!")
            game_over = True
        else:
            if not st.session_state.game_over:
                if(st.session_state.Hit):
                    st.session_state.player_cards.append(st.session_state.deck.pop())
                    st.session_state.player_score = calculate_hand(st.session_state.player_cards)
                    st.empty()
                    printcard(st, card_images)
                    if st.session_state.player_score > 21:
                        st.error("Bust! You lose!")
                        game_over = True
                        st.session_state.hit = False
                        st.session_state.stand = False
                    elif st.session_state.player_score == 21:
                        st.success("Blackjack! You win!")
                        game_over = True
                        st.session_state.hit = False
                        st.session_state.stand = False
                elif (st.session_state.Stand):
                    while st.session_state.dealer_score < 17:
                        st.session_state.dealer_cards.append(st.session_state.deck.pop())
                        st.session_state.dealer_score = calculate_hand(st.session_state.dealer_cards)
                    st.empty()
                    printcard(st, card_images)
                    if st.session_state.dealer_score > 21:
                        st.success("Dealer bust! You win!")
                        game_over = True
                    elif st.session_state.dealer_score == 21:
                        st.error("Dealer got Blackjack! You lose!")
                        game_over = True
                    elif st.session_state.dealer_score > st.session_state.player_score:
                        st.error("You lose!")
                        game_over = True
                    elif st.session_state.dealer_score < st.session_state.player_score:
                        st.success("You win!")
                        game_over = True
                    else:
                        st.warning("It's a tie!")
                        game_over = True
    #directly start after shuffling
    else:
        if st.session_state.player_score > 0:
            if st.session_state.player_score == 21:
                st.session_state.player_score = calculate_hand(st.session_state.player_cards)
                st.empty()
                st.success("Blackjack! You win!")
                game_over = True
            else:
                if not st.session_state.game_over:
                    if(st.session_state.Hit):
                        st.session_state.player_cards.append(st.session_state.deck.pop())
                        st.session_state.player_score = calculate_hand(st.session_state.player_cards)
                        st.empty()
                        printcard(st, card_images)
                
                        if st.session_state.player_score > 21:
                            st.error("Bust! You lose!")
                            st.session_state.game_over = True
                            st.session_state.hit = False
                            st.session_state.stand = False
                        elif st.session_state.player_score == 21:
                            st.session_state.player_score = calculate_hand(st.session_state.player_cards)
                            st.success("Blackjack! You win!")
                            st.session_state.game_over = True
                            st.session_state.hit = False
                            st.session_state.stand = False
                    elif (st.session_state.Stand):
                        while st.session_state.dealer_score < 17:
                            st.session_state.dealer_cards.append(st.session_state.deck.pop())
                            st.session_state.dealer_score = calculate_hand(st.session_state.dealer_cards)
                        st.empty()
                        printcard(st, card_images)

                        if st.session_state.dealer_score > 21:
                            st.success("Dealer bust! You win!")
                            game_over = True
                        elif st.session_state.dealer_score == 21:
                            st.error("Dealer got Blackjack! You lose!")
                            game_over = True
                        elif st.session_state.dealer_score > st.session_state.player_score:
                            st.error("You lose!")
                            game_over = True
                        elif st.session_state.dealer_score < st.session_state.player_score:
                            st.success("You win!")
                            game_over = True
                        else:
                            st.warning("It's a tie!")
                            game_over = True
