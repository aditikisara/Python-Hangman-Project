# Random words list

import tkinter as tk
import random

def check_dash():
    if '_' not in dashes:
        prompt.configure(text = "You win! Exiting...")
        window.after(2000, window.destroy)

def check_let(letter, word):
    if letter in let_guess_list:
        prompt.configure(text = "You already guessed that letter!")
    else:
        let_guess_list.append(letter)
        let_guessed.configure(text = "Letters guessed: " + str(let_guess_list))
        if letter in word:
            prompt.configure(text = "That letter is in the word!")
            result = ""
            for i in range (len(word)):
                if letter == word[i]:
                    dashes[i] = letter
                    result = dashes
                    dash.configure(text = result)
        else:
            prompt.configure(text = "That letter is not in the word.")
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
        prompt.configure(text = "Game over! The word was: " + str(word) + ". Exiting...")
        #window.after(2000, window.destroy)


def clicked(letter, word):
    check_let(letter, word)
    check_dash()

# -----------word = joker---------------------------
FILE = "words.txt"

f = open("words.txt")
word_lst = []
for line in f:
    word_lst.append(line.strip())

word = random.choice(word_lst)
#print("The word is:", word)

dashes = []
for i in word:
    dashes.append('_')

let_guess_list = []

window = tk.Tk()
window.title("Hangman")

heading = tk.Label(window, text = "Welcome to Hangman! I'm thinking of a word... try to guess it!")
heading.grid(row = 1, column = 1, columnspan = 2)

num_guess_left = tk.Label(window, text = "Hint: School")
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

alphabet = tk.Frame()
alphabet.grid(row = 3, column = 2, columnspan = 1)


a = tk.Button(alphabet, text = "a", command=lambda: clicked("A", word))
a.grid(row = 3, column = 1)
b = tk.Button(alphabet, text = "b", command=lambda: clicked("B", word))
b.grid(row = 3, column = 2)
c = tk.Button(alphabet, text = "c", command=lambda: clicked("C", word))
c.grid(row = 3, column = 3)
d = tk.Button(alphabet, text = "d", command=lambda: clicked("D", word))
d.grid(row = 3, column = 4)
e = tk.Button(alphabet, text = "e", command=lambda: clicked("E", word))
e.grid(row = 3, column = 5)

f = tk.Button(alphabet, text = "f", command=lambda: clicked("F", word))
f.grid(row = 3, column = 6)
g = tk.Button(alphabet, text = "g", command=lambda: clicked("G", word))
g.grid(row = 3, column = 7)
h = tk.Button(alphabet, text = "h", command=lambda: clicked("H", word))
h.grid(row = 3, column = 8)
i = tk.Button(alphabet, text = "i", command=lambda: clicked("I", word))
i.grid(row = 3, column = 9)
j = tk.Button(alphabet, text = "j", command=lambda: clicked("J", word))
j.grid(row = 3, column = 10)

k = tk.Button(alphabet, text = "k", command=lambda: clicked("K", word))
k.grid(row = 3, column = 11)
l = tk.Button(alphabet, text = "l", command=lambda: clicked("L", word))
l.grid(row = 3, column = 12)
m = tk.Button(alphabet, text = "m", command=lambda: clicked("M", word))
m.grid(row = 3, column = 13)
n = tk.Button(alphabet, text = "n", command=lambda: clicked("N", word))
n.grid(row = 4, column = 1)
o = tk.Button(alphabet, text = "o", command=lambda: clicked("O", word))
o.grid(row = 4, column = 2)

p = tk.Button(alphabet, text = "p", command=lambda: clicked("P", word))
p.grid(row = 4, column = 3)
q = tk.Button(alphabet, text = "q", command=lambda: clicked("Q", word))
q.grid(row = 4, column = 4)
r = tk.Button(alphabet, text = "r", command=lambda: clicked("R", word))
r.grid(row = 4, column = 5)
s = tk.Button(alphabet, text = "s", command=lambda: clicked("S", word))
s.grid(row = 4, column = 6)
t = tk.Button(alphabet, text = "t", command=lambda: clicked("T", word))
t.grid(row = 4, column = 7)

u = tk.Button(alphabet, text = "u", command=lambda: clicked("U", word))
u.grid(row = 4, column = 8)
v = tk.Button(alphabet, text = "v", command=lambda: clicked("V", word))
v.grid(row = 4, column = 9)
w = tk.Button(alphabet, text = "w", command=lambda: clicked("W", word))
w.grid(row = 4, column = 10)
x = tk.Button(alphabet, text = "x", command=lambda: clicked("X", word))
x.grid(row = 4, column = 11)
y = tk.Button(alphabet, text = "y", command=lambda: clicked("Y", word))
y.grid(row = 4, column = 12)
z = tk.Button(alphabet, text = "z", command=lambda: clicked("Z", word))
z.grid(row = 4, column = 13)

let_guessed = tk.Label(text = "Letter guessed: " + str(let_guess_list))
let_guessed.grid(row = 4, column = 1, columnspan = 2)

prompt = tk.Label(text = "")
prompt.grid(row = 5, column = 1, columnspan = 2)

dash = tk.Label(text = dashes)
dash.grid(row = 6, column = 1, columnspan = 2)

window.mainloop()