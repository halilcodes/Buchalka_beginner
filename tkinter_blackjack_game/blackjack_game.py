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


# def deal_dealer():  # not working
#     global dealerScore, dealerPoints
#     value, card = random.choice(deck)
#     score = tk.getint(dealerScore) + value
#
#     dealerPoints.configure(textvariable=score)


window = tk.Tk()
bg_color = "#116D6E"
fg_color = "white"


deck = []
load_images(deck)

# Set up the screen and frames for the dealer and the player
window.title("Black Jack")
window.geometry("640x480")
window.configure(background=bg_color)

result_text = tk.StringVar()
result = tk.Label(window, textvariable=result_text, font=('bold', 15), background=bg_color, foreground=fg_color)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tk.Frame(window, relief="sunken", borderwidth=1, background=bg_color)
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)


dealerScore = tk.IntVar()
dealerLabel = tk.Label(cardFrame, text='Dealer', font=('bold', 15), background=bg_color, foreground=fg_color)
dealerLabel.grid(row=0, column=0)
dealerPoints = tk.Label(cardFrame, textvariable=dealerScore, background=bg_color, fg=fg_color, font=('bold', 15))
dealerPoints.grid(row=1, column=0)

playerScore = tk.IntVar()
playerLabel = tk.Label(cardFrame, text='Player', font=('bold', 15), background=bg_color, foreground=fg_color)
playerLabel.grid(row=2, column=0)
playerPoints = tk.Label(cardFrame, textvariable=playerScore, background=bg_color, fg=fg_color, font=('bold', 15))
playerPoints.grid(row=3, column=0)

hitButton = tk.Button(text='Hit!')
stopButton = tk.Button(text='Stop')
hitButton.grid(row=5, column=1)
stopButton.grid(row=5, column=2)
newGameButton = tk.Button(text='New Game')
newGameButton.grid(row=6, column=1)
shuffleButton = tk.Button(text='Shuffle')
shuffleButton.grid(row=6, column=2)

window.mainloop()
