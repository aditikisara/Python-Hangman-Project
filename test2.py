# Array of buttons

import tkinter as tk
import random

def check_dash():
    if '_' not in dashes:
        prompt.configure(text = "You win! Exiting...")
        window.after(2000, window.destroy)

def check_let(letter):
    if letter in let_guess_list:
        prompt.configure(text = "You already guessed that letter!")
    else:
        let_guess_list.append(letter)
        let_guessed.configure(text = "Letters guessed: " + str(let_guess_list))
        if letter not in "joker":
            hangman()

def hangman():
    h = hanger.cget("text")
    # If case 0, then case 1
    if h == "  _____ \n |        |\n           | \n           | \n           | \n __________":
        hanger.configure(text = "  _____ \n |        |\n  O       | \n            | \n            | \n __________")
    
    # If case 1, then case 2
    elif h == "  _____ \n |        |\n  O       | \n            | \n            | \n __________":
        hanger.configure(text = "  _____ \n |        |\n  O       | \n   |        | \n            | \n __________")
    
    # If case 2, then case 3
    elif h == "  _____ \n |        |\n  O       | \n   |        | \n            | \n __________":
        hanger.configure(text = "  _____ \n |        |\n  O       | \n   |        | \n  /         | \n __________")
    
    # If case 3, then case 4
    elif h == "  _____ \n |        |\n  O       | \n   |        | \n  /         | \n __________":
        hanger.configure(text = "  _____ \n |        |\n  O       | \n   |        | \n  / \       | \n __________")
    
    # If case 4, then case 5
    elif h == "  _____ \n |        |\n  O       | \n   |        | \n  / \       | \n __________":
        hanger.configure(text = "  _____ \n |        |\n  O       | \n  /|       | \n  / \      | \n __________")
    
    # If case 5, then case 6
    elif h == "  _____ \n |        |\n  O       | \n  /|       | \n  / \      | \n __________":
        hanger.configure(text = "  _____ \n |        |\n  O       | \n  /|\      | \n  / \      | \n __________")
        prompt.configure(text = "Game over! The word was: JOKER. Exiting...")
        window.after(2000, window.destroy)


def clicked(letter):

    print(letter)

    """
    if letter in let_guess_list:
        prompt.configure(text = "You already guessed this letter!")

    if letter == "j":
        prompt.configure(text = "That letter is in the word!")
        dashes[0] = "J"
        dash.configure(text = dashes)
        check_dash()
        check_let("j")
    
    elif letter == "o":
        prompt.configure(text = "That letter is in the word!")
        dashes[1] = "O"
        dash.configure(text = dashes)
        check_dash()
        check_let("o")
    
    elif letter == "k":
        prompt.configure(text = "That letter is in the word!")
        dashes[2] = "K"
        dash.configure(text = dashes)
        check_dash()
        check_let("k")
    
    elif letter == "e":
        prompt.configure(text = "That letter is in the word!")
        dashes[3] = "E"
        dash.configure(text = dashes)
        check_dash()
        check_let("e")
    
    elif letter == "r":
        prompt.configure(text = "That letter is in the word!")
        dashes[4] = "R"
        dash.configure(text = dashes)
        check_dash()
        check_let("r")

    else:
        prompt.configure(text = "That letter is not in the word.")
        check_let(letter)
    """
# -----------word = joker---------------------------
dashes = ['_', '_', '_', '_', '_']
let_guess_list = []

window = tk.Tk()
window.title("Hangman")

heading = tk.Label(window, text = "Welcome to Hangman! I'm thinking of a word... try to guess it!")
heading.grid(row = 1, column = 1, columnspan = 2)

num_guess_left = tk.Label(window, text = "Hint: Villain")
num_guess_left.grid(row = 2, column = 1, columnspan = 2)

hanger = tk.Label(window, text = "  _____ \n |        |\n           | \n           | \n           | \n __________")
hanger.grid(row = 3, column = 1, columnspan = 1)

"""
DO NOT CHANGE
0. "  _____ \n |        |\n           | \n           | \n           | \n __________"
1. "  _____ \n |        |\n  O       | \n            | \n            | \n __________"
2. "  _____ \n |        |\n  O       | \n   |        | \n            | \n __________"
3. "  _____ \n |        |\n  O       | \n   |        | \n  /         | \n __________"
4. "  _____ \n |        |\n  O       | \n   |        | \n  / \       | \n __________"
5. "  _____ \n |        |\n  O       | \n  /|       | \n  / \      | \n __________"
6. "  _____ \n |        |\n  O       | \n  /|\      | \n  / \      | \n __________"
"""

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
beta = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabeta = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = tk.Frame()
alphabet.grid(row = 3, column = 2, columnspan = 1)

for i in range (13):
    for j in range (2):
        row1 = tk.Button(alphabet, text = alpha[i], command=lambda: clicked(alpha[i]))
        row1.grid(row = 3, column = i)
        row2 = tk.Button(alphabet, text = beta[i], command=lambda: clicked(beta[i]))
        row2.grid(row = 4, column = i)

let_guessed = tk.Label(text = "Letter guessed: " + str(let_guess_list))
let_guessed.grid(row = 4, column = 1, columnspan = 2)

prompt = tk.Label(text = "")
prompt.grid(row = 5, column = 1, columnspan = 2)

dash = tk.Label(text = dashes)
dash.grid(row = 6, column = 1, columnspan = 2)

window.mainloop()