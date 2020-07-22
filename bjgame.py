# blackjack game

# Process
# Player Cards First (2)
# Dealer Cards Next (2)
# Display Player Cards to User
# Sum of the Dealer Cards
# Sum of the Player Cards
# Compare the sums of the cards between D v P
# If P card sum > 21 = BUST
# Loop If P card is <=21 = Twist or Stick (Try)
# P twists again - Check <=21 condition else, Stick.
# Check Dealers Cards
# Dealer compares his two cards with total sum of the player cards (14 - 19)
# Dealer >= Player Cards = Dealer Wins
# If Dealer cards >21 = BUST

import random
import time

global std_deck


def deal_and_display():
    std_deck = [
        # 2 3 4 5 6 7 8 9 10  J  Q  K  A
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    ]

    c1 = std_deck.pop(random.randrange(len(std_deck)))
    c2 = std_deck.pop(random.randrange(len(std_deck)))
    print("Player has: " + str(c1) + " and " + str(c2) + "\nTotal = " + str(c1 + c2))

    d1 = std_deck.pop(random.randrange(len(std_deck)))
    d2 = std_deck.pop(random.randrange(len(std_deck)))
    print("Dealer has: " + str(d1) + " and " + str(d2) + "\nTotal = " + str(d1 + d2))

    player_total = c1 + c2
    dealer_total = d1 + d2

    while player_total <= 21:
        c3 = std_deck.pop(random.randrange(len(std_deck)))
        choice = input("Player total is: " + (str(player_total) + " - Would you like to [S]tick or [T]wist?: "))
        if choice == "S":
            print("Player has: " + (str(player_total)))
            break
            # Move onto Dealers Turn
        elif choice == "T":
            time.sleep(0.5)
            print("New card is a " + str(c3))
            player_total += c3

    if player_total > 21:
        print("Player has bust with " + str(player_total))
        print("\nNEW GAME!\n")
        deal_and_display()

    while dealer_total <= 21:
        d3 = std_deck.pop(random.randrange(len(std_deck)))
        print("Dealer has: " + str(dealer_total))
        time.sleep(2)
        try:
            if dealer_total < player_total:
                print("Dealer draws")
                time.sleep(1)
                dealer_total += int(d3)
                time.sleep(1)
                print("New card is a " + str(d3))
        except:
            if dealer_total == 17:
                print("Dealer sticks with 17")
                break
        if dealer_total > 21:
            time.sleep(1)
            print("Dealer busts with " + str(dealer_total))
            print("\nNEW GAME!\n")
            time.sleep(1)
            deal_and_display()
        if dealer_total >= player_total or player_total > 21:
            time.sleep(1)
            print("Dealer wins with " + str(dealer_total))
            time.sleep(1)
            print("\nNEW GAME!\n")
            deal_and_display()
        if (dealer_total > player_total) and (dealer_total <= 21):
            time.sleep(1)
            print("Dealer wins!")
            print("\nNEW GAME!\n")
            time.sleep(1)
            deal_and_display()


deal_and_display()
