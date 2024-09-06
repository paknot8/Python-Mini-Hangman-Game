import random

word = ["apple","carrot","banana","pear"] # the list
chosenWord = random.choice(word) # choose a random word
displayWord = ['_' for _ in chosenWord] # show underscores instead of the words in the list for every word
attempt = 10 # how many attempts you can answer wrong

#======================= Methods ======================================
def StartHangmanGame():
    print("--- Welcome to the Hangman Game! ---")
    CheckGuess()
    WinOrLose()

def CheckGuess():
    while attempt > 0 and '_' in displayWord:
        print("\n" + ' '.join(displayWord)) # join all elements together with an extra space
        guess = input("Guess a letter: ").lower()
        if guess in chosenWord:
            for index, letter in enumerate(chosenWord): # gives access to the index and the letter of that chosen word
                if letter == guess:
                    displayWord[index] = guess # reveal the letter
        else:
            attempt -= 1
            print("Letter does not appear in the word. current wrong attempts left: " + str(attempt))

def WinOrLose():
    if '_' not in displayWord:
        print("Congratulations! You have correctly guessed the word!")
        print(' '.join(displayWord))
        print("You survived!")
    else:
        print("Oh no! You have run out of attempts. Game Over!")
        print("You Lost!")