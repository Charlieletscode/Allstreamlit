import pygame
import random

# Set up the deck of cards
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

deck = []
for suit in suits:
    for rank in ranks:
        deck.append((rank, suit))

# Define the value of each card
card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    'ace': 11,
}

# Load card images
card_images = {}
for suit in suits:
    for rank in ranks:
        filename = f'source/images/{rank}_of_{suit}.png'
        card_images[(rank, suit)] = pygame.image.load(filename)

# Define the deal function
def deal():
    return [deck.pop(random.randint(0, len(deck)-1)) for i in range(2)]

# Define the hit function
def hit(hand):
    hand.append(deck.pop(random.randint(0, len(deck)-1)))
    return hand

# Define the score function
def score(hand):
    score = 0
    aces = 0
    for card in hand:
        value = card_values[card[0]]
        score += value
        if card[0] == 'A':
            aces += 1
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack")

# Load background image
background_image = pygame.image.load('source/images/background.png')

# Set up the fonts
FONT_LARGE = pygame.font.Font(None, 48)
FONT_MEDIUM = pygame.font.Font(None, 32)
FONT_SMALL = pygame.font.Font(None, 24)

# Define the main function
def main():
    # Set up the game
    player_hand = deal()
    dealer_hand = deal()
    player_score = score(player_hand)
    dealer_score = score(dealer_hand)

    # Set up the gambling system
    balance = 100
    bet = 0

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Clicked on "Deal" button
                    if deal_button_rect.collidepoint(event.pos):
                        # Deal new hands
                        player_hand = deal()
                        dealer_hand = deal()
                        player_score = score(player_hand)
                        dealer_score = score(dealer_hand)
                        # Reset bet and show new balance
                        balance -= bet
                        bet = 0
                        # Check for blackjack
                        if player_score == 21:
                            balance += bet * 2.5
                    # Clicked on "Hit" button
                    elif hit_button_rect.collidepoint(event.pos):
                        # Hit the player's hand
                        player_hand = hit(player_hand)
                        player_score = score(player_hand)
                        # Check for bust
                        if player_score > 21:
                            balance -= bet
                            bet = 0
                    # Clicked on "Stand" button
                    elif stand_button_rect.collidepoint(event.pos):
                        # Dealer's turn
                        while dealer_score < 17:
                            dealer_hand = hit(dealer_hand)
                            dealer_score = score(dealer_hand)
                        # Determine winner
                        if dealer_score > 21:
                            balance += bet * 2
                        elif dealer_score > player_score:
                            balance -= bet
                        elif player_score > dealer_score:
                            balance += bet * 2
                        else:
                            balance += bet
                        # Deal new hands and reset bet
                        player_hand = deal()
                        dealer_hand = deal()
                        player_score = score(player_hand)
                        dealer_score = score(dealer_hand)
                        bet = 0
                    # Clicked on "Increase Bet" button
                    elif increase_bet_button_rect.collidepoint(event.pos):
                        if balance >= 10:
                            balance -= 10
                            bet += 10
                    # Clicked on "Decrease Bet" button
                    elif decrease_bet_button_rect.collidepoint(event.pos):
                        if bet >= 10:
                            balance += 10
                            bet -= 10

        # Draw the screen
        screen.blit(background_image, (0, 0))

        # Draw the player's hand
        x = 50
        y = 400
        for card in player_hand:
            screen.blit(card_images[card], (x, y))
            x += 100
        text = FONT_SMALL.render(f'Score: {player_score}', True, (255, 255, 255))
        screen.blit(text, (50, 370))

        # Draw the dealer's hand
        x = 50
        y = 100
        for i, card in enumerate(dealer_hand):
            if i == 0:
                screen.blit(card_images[('back', 'red')], (x, y))
            else:
                screen.blit(card_images[card], (x, y))
            x += 100
        if dealer_score == 21:
            text = FONT_SMALL.render('Blackjack', True, (255, 255, 255))
            screen.blit(text, (50, 70))
        elif dealer_score > 0:
            text = FONT_SMALL.render(f'Score: {dealer_score}', True, (255, 255, 255))
            screen.blit(text, (50, 70))

        # Draw the gambling system
        text = FONT_SMALL.render(f'Balance: ${balance}', True, (255, 255, 255))
        screen.blit(text, (550, 550))
        text = FONT_SMALL.render(f'Bet: ${bet}', True, (255, 255, 255))
        screen.blit(text, (550, 520))

        # Draw the buttons
        deal_button_rect = pygame.draw.rect(screen, (0, 255, 0), (650, 400, 100, 50))
        text = FONT_SMALL.render('Deal', True, (255, 255, 255))
        screen.blit(text, (665, 415))
        hit_button_rect = pygame.draw.rect(screen, (0, 0, 255), (650, 470, 100, 50))
        text = FONT_SMALL.render('Hit', True, (255, 255, 255))

        for i, card in enumerate(dealer_hand):
            if i == 0:
                # Draw the back of the card for the first dealer card
                screen.blit(card_images[('back', 'red')], (x, y))
            else:
                screen.blit(card_images[card], (x, y))
            x += 100
        text = FONT_SMALL.render(f'Dealer score: {dealer_score}', True, (255, 255, 255))
        screen.blit(text, (50, 70))

        # Draw the buttons
        deal_button_rect = pygame.Rect(600, 100, 100, 50)
        pygame.draw.rect(screen, (0, 0, 0), deal_button_rect)
        text = FONT_MEDIUM.render('Deal', True, (255, 255, 255))
        screen.blit(text, (610, 110))

        hit_button_rect = pygame.Rect(600, 200, 100, 50)
        pygame.draw.rect(screen, (0, 0, 0), hit_button_rect)
        text = FONT_MEDIUM.render('Hit', True, (255, 255, 255))
        screen.blit(text, (610, 210))

        stand_button_rect = pygame.Rect(600, 300, 100, 50)
        pygame.draw.rect(screen, (0, 0, 0), stand_button_rect)
        text = FONT_MEDIUM.render('Stand', True, (255, 255, 255))
        screen.blit(text, (610, 310))

        increase_bet_button_rect = pygame.Rect(600, 400, 100, 50)
        pygame.draw.rect(screen, (0, 0, 0), increase_bet_button_rect)
        text = FONT_SMALL.render('+10', True, (255, 255, 255))
        screen.blit(text, (615, 410))

        decrease_bet_button_rect = pygame.Rect(600, 450, 100, 50)
        pygame.draw.rect(screen, (0, 0, 0), decrease_bet_button_rect)
        text = FONT_SMALL.render('-10', True, (255, 255, 255))
        screen.blit(text, (615, 460))

        # Draw the balance and bet
        text = FONT_LARGE.render(f'Balance: ${balance}', True, (255, 255, 255))
        screen.blit(text, (50, 20))
        text = FONT_MEDIUM.render(f'Bet: ${bet}', True, (255, 255, 255))
        screen.blit(text, (610, 20))

        # Update the display
        pygame.display.update()

if __name__ == '__main__':
    main()