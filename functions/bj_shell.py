""" blackjack shell game """
import pprint
import random

player_lead = 0
dealer_lead = 0


def deal_card():
    global deck
    return deck.pop(random.randint(1, len(deck) - 1))


def shuffle():
    cards = []

    for each in ["spade", "heart", "diamond", "club"]:
        for num in range(1, 14):
            card = f"{num} of {each}"
            value = num if num < 11 else 10
            value = 10 if num == 1 else value
            cards.append((value, card))
    return cards


def calculate_score(hand: list) -> int:
    score = 0
    for card in hand:
        score += card[0]
    return score


def show_hand(who, hand):
    print(f"{who}: {hand} - - score: {calculate_score(hand)}")
    return None


def play_bj():
    global player_lead, dealer_lead
    dealer_hand = [deal_card()]
    show_hand("dealer", dealer_hand)

    player_hand = [deal_card(), deal_card()]
    show_hand("player", player_hand)

    choice = int(input("1: Hit\nelse: Hold\n: "))

    while choice == 1:
        player_hand.append(deal_card())
        show_hand("player", player_hand)

        if calculate_score(player_hand) > 21:
            print("YOU LOST, went over 21")
            dealer_lead += 1
            print(f"Dealer: {dealer_lead} - - Player: {player_lead}")
            break

        choice = int(input("1: Hit\nelse: Hold\n"))

    if calculate_score(player_hand) < 22:
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())
        show_hand("dealer", dealer_hand)
        if calculate_score(dealer_hand) > 21:
            print("YOU WIN, dealer over 21")
            player_lead += 1
            print(f"Dealer: {dealer_lead} - - Player: {player_lead}")

        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        if player_score == dealer_score:
            print("DRAW!")
        elif dealer_score < player_score < 22:
            print("YOU WIN")
            player_lead += 1
            print(f"Dealer: {dealer_lead} - - Player: {player_lead}")
        elif player_score < dealer_score < 22:
            print("YOU LOST")
            dealer_lead += 1
            print(f"Dealer: {dealer_lead} - - Player: {player_lead}")


if __name__ == "__main__":
    new_game = 1
    deck = shuffle()
    while new_game == 1:
        wanna_shuffle = int(input("Wanna shuffle?? 1/0: "))
        if wanna_shuffle:
            deck = shuffle()
        play_bj()

        new_game = int(input("Wanna keep playing? 1/0: "))
    print("Remaining deck: ")
    pprint.pprint(deck)
