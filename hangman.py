"""
HANGMAN: The program picks a random word from the list given and the user has to guess
what the word is. They are given a maximum of 10 chances to guess the word.
"""
import random
import sys

FILE = "words.txt"    # File to read word list from

def main():
    """
    Lines 15 - 18 open the corresponding text document, reads the list of words, and 
    appends them into a list called "lst". It also strips away any unnecessary characters.
    """

    f = open("words.txt")
    lst = []
    for line in f:
        lst.append(line.strip())
    
    """
    These are the variables used in the program ---
    word: gives a random word from lst
    dashes: creates the appropriate amount of dashes for the word
    num_guess: sets the max number of guesses the user has
    """

    word = random.choice(lst)
    dashes = []
    letters_guessed = []

    # This is the number of wrong tries the user has.  
    num_guess = 6
    
    for i in word:
        dashes.append('_')
    
    #Used for testing
    #print(word)

    """
    Print the welcome statement and provide the correct number of dashes.
    """

    print("")
    print("Welcome to Hangman! Enter a letter to guess! \nEnter '!' to guess the word or '1' to give up.")
    print("Hint: School")
    print(dashes)
    print("")

    while (num_guess > 1):
        for i in range (len(word)):
            print("Lives left:", num_guess)
            letter = input("Guess a letter: ")
            
            # Convert letter to uppercase
            letter = letter.upper()

            # If the user wants to guess the word
            if letter == "!":
                guess = input("Enter your guess: ")
                guess = guess.upper()
                if guess == word:
                    print("You guessed the word!")
                    sys.exit()
                else:
                    print("That's not quite right...")
                    letter = input("Guess a letter: ")
            
            # If the user gives up
            if letter == "1":
                print("You gave up. The word was", word)
                sys.exit()

            # If the length of the input is bigger than 1 character
            if len(letter) > 1:
                print("")
                print("Enter only one character")
                continue
            
            # If the user already guessed the letter
            if letter in letters_guessed:
                print("You already guessed that letter!")
                print("")
                continue

            # Append the letter into the letters_guessed list and print them out
            letters_guessed.append(letter)
            print("Letters guessed: ", letters_guessed)

            dashupd(letter, dashes, word)
            if letter not in word:
                num_guess -= 1
                # When user runs out of guesses
                if num_guess == 0:
                    print("Lives left: 0")
                    print("")
                    print("The word was", word)
                    sys.exit()
            print("")

            # If there are no more dashes left in the dashes list, then end the program
            if "_" not in dashes:
                print("You win!")
                num_guess = 0
                sys.exit()

    # Print out what the word was if they didn't guess in time
    print("The word was", word)

"""
This function updates the amount of dashes in the list and adds the corresponding letter 
in the list (if it exists).
"""

def dashupd(letter, dashes, word):
    result = ""

    if letter in word:
        print("That letter is in the word!")
        for i in range(len(word)):
            if letter == word[i]:
                dashes[i] = letter
                result = dashes
        
        print(result)

    else:
        print("That letter is not in the word.")
        result = dashes
        print(result)

if __name__ == "__main__":
    main()