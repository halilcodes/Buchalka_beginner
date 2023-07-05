import pprint
import tkinter
import tkinter as tk
import random

dealer_hand = []
player_hand = []
dealer_score = 0
player_score = 0


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    if tk.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = "cards\\{}_{}.{}".format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((card, image))
        # for the face cards
        for card in face_cards:
            name = "cards\\{}_{}.{}".format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((10, image))


def deal_dealer():
    global deck, dealer_hand, dealer_score, dealer_card_frame, playerScoreLabel
    # clear current frame
    for widget in dealer_card_frame.winfo_children():
        widget.destroy()
    # choose card
    random_card = deck.pop(random.randint(1, len(deck)-1))
    dealer_hand.append(random_card)
    # add score
    dealer_score = calculate_score(dealer_hand)
    dealerScoreLabel.set(dealer_score)
    dealer_card_frame.update()
    # add images
    for card in dealer_hand:
        _, image = card
        img = tk.Button(dealer_card_frame, image=image)
        img.pack(side=tk.LEFT)
    return random_card[1]


def play_dealer():
    global dealer_hand, player_hand
    current_score = calculate_score(dealer_hand)
    while current_score < 17:
        deal_dealer()
        current_score = calculate_score(dealer_hand)
    if current_score > 21 or dealer_score < player_score < 21:
        result_text.set("PLAYER WON!")
        window.update()
    elif current_score == calculate_score(player_hand):
        result_text.set("DRAW!")
        window.update()


def deal_player():
    global deck, player_hand, player_score, player_card_frame, playerScoreLabel
    # clear current frame
    for widget in player_card_frame.winfo_children():
        widget.destroy()
    # choose card
    random_card = deck.pop(random.randint(1, len(deck)-1))
    player_hand.append(random_card)
    # add score
    player_score = calculate_score(player_hand)
    playerScoreLabel.set(player_score)
    player_card_frame.update()
    # add image
    for card in player_hand:
        _, image = card
        img = tk.Button(player_card_frame, image=image)
        img.pack(side=tk.LEFT)
    # check if lost
    if player_score > 21:
        result_text.set("DEALER WON!")
        window.update()
    elif player_score == 21:
        result_text.set("PLAYER WON!! BLACKJACK!")
    return None


def calculate_score(hand):
    total_list = []
    score = 0
    for card in hand:
        value, _ = card
        total_list.append(value)
    score = sum(total_list)
    if 1 in total_list:
        score += 10
        if score > 21:
            score -= 10
    return score


def shuffle_cards():
    global deck
    deck = []
    load_images(deck)
    return None


def play_bj():
    global dealer_hand, player_hand, dealer_score, player_score, window
    result_text.set("NEW GAME...")
    window.update()
    dealer_hand = []
    player_hand = []
    dealer_score = 0
    player_score = 0
    deal_dealer()
    deal_player()
    deal_player()


window = tk.Tk()
bg_color = "#116D6E"
fg_color = "white"
font = ('bold', 15)
# Set up the screen and frames for the dealer and the player
window.title("Black Jack")
window.geometry("640x480")
window.configure(background=bg_color)

deck = []
load_images(deck)
# pprint.pprint(deck)

# 1 - Top is reserved for info
result_text = tk.StringVar()
result = tk.Label(window, textvariable=result_text, font=font, background=bg_color, foreground=fg_color)
result.grid(row=0, column=0, columnspan=3)


# 2- mid-section (cardFrame) is for game info
cardFrame = tk.Frame(window, relief="sunken", borderwidth=1, background=bg_color)
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealerScoreLabel = tk.IntVar()
tk.Label(cardFrame, text='Dealer', font=font, background=bg_color, foreground=fg_color).grid(row=0, column=0)
tk.Label(cardFrame, textvariable=dealerScoreLabel, background=bg_color, fg=fg_color, font=font).grid(row=1, column=0)

playerScoreLabel = tk.IntVar()
tk.Label(cardFrame, text='Player', font=font, background=bg_color, foreground=fg_color).grid(row=2, column=0)
tk.Label(cardFrame, textvariable=playerScoreLabel, background=bg_color, fg=fg_color, font=font).grid(row=3, column=0)

# Frame to hold the card images
dealer_card_frame = tk.Frame(cardFrame, background=bg_color)
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="ew")
player_card_frame = tk.Frame(cardFrame, background=bg_color)
player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')


# 3- Bottom frame reserved for Button configurations
buttonFrame = tkinter.Frame(window, background=bg_color)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky="w")
hitButton = tk.Button(buttonFrame, text='Hit!', command=deal_player)
stopButton = tk.Button(buttonFrame, text='Stop', command=play_dealer)
hitButton.grid(row=0, column=0, sticky="ew")
stopButton.grid(row=0, column=1, sticky="ew")
newGameButton = tk.Button(buttonFrame, text='New Game', command=play_bj)
newGameButton.grid(row=1, column=0, sticky="ew")
shuffleButton = tk.Button(buttonFrame, text='Shuffle', command=shuffle_cards)
shuffleButton.grid(row=1, column=1, sticky="ew")

play_bj()

window.mainloop()
