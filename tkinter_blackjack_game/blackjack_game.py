import tkinter as tk
import random


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
            card_images.append((card, image,))
        # for the face cards
        for card in face_cards:
            name = "cards\\{}_{}.{}".format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_dealer():
    value, card = random.choice(cards)
    value_label = tk.Label(window, text=value, font=('bold', 15), background=bg_color, foreground=fg_color)
    value_label.grid(row=0, column=0)





window = tk.Tk()
bg_color = "#116D6E"
fg_color = "white"


cards = []
load_images(cards)

# Set up the screen and frames for the dealer and the player
window.title("Black Jack")
window.geometry("640x480")
window.configure(background=bg_color)

dealerLabel = tk.Label(window, text='Dealer', font=('bold', 15), background=bg_color, foreground=fg_color)
dealerLabel.grid(row=0, column=1, columnspan=3)

playerLabel = tk.Label(text='Player', font=('bold', 15), background=bg_color, foreground=fg_color)
playerLabel.grid(row=4, column=1, columnspan=3)


hitButton = tk.Button(text='Hit!')
stopButton = tk.Button(text='Stop')
hitButton.grid(row=5, column=1)
stopButton.grid(row=5, column=2)
newGameButton = tk.Button(text='New Game', command=deal_dealer)
newGameButton.grid(row=6, column=1)
shuffleButton = tk.Button(text='Shuffle')
shuffleButton.grid(row=6, column=2)

window.mainloop()
