# Python-Hangman-Project

I coded a hangman game based on a text file of certain words. The program will read through the words in the text file and input them in a list. Then it will pick a random word from the list and generate the appropriate number of dashes. The user will then guess letter by letter what the word is. They are given 6 "lives" (the number of wrong attempts that they have) and need to guess the word before the number of lives run out. They are also given an option to guess the whole word in one attempt. When the user guesses the word correctly within the number of lives or when the number of lives run out, the program reveals the word and terminates.

There are two versions of this program.

The first one is coded in simple Python and is run in a terminal. The second one is coded in Python using an available GUI called "Tkinter". This was my first experience with working with a GUI, and I taught myself everything I know from scratch. In this version, a pop-up window will appear, where the game is displayed. An actual drawing of the Hangman game is displayed and changes depending on the letter the user enters. The window will automatically close when the game ends.

In the future, I would like to add a mechanic that will allow a user to play again if they choose to. This would require me to declare a boolean variable called "playAgain" set to true (meaning the game is played). Then I would modify the main while loop to account for this. After the while loop, playAgain would be set to "false". Then the program will prompt the user if they want to play again. If they select yes, then playAgain will be set to true and the while loop iterates again. If they select no, then the program will terminate.
