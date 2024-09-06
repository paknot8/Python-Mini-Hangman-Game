import random

# Constants
WORDS = ["apple", "carrot", "banana", "pear"]
MAX_ATTEMPTS = 10

def start_hangman_game():
    """Starts a new game of Hangman."""
    print("--- Welcome to the Hangman Game! ---")
    chosen_word = random.choice(WORDS)
    display_word = ['_' for _ in chosen_word]
    play_game(chosen_word, display_word, MAX_ATTEMPTS)
    win_or_lose(display_word, chosen_word)

def play_game(chosen_word, display_word, attempts):
    """Plays the game of Hangman."""
    while attempts > 0 and '_' in display_word:
        print("\n" + ' '.join(display_word))
        guess = input("Guess a letter: ").lower()
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display_word[index] = guess
        else:
            attempts -= 1
            print("Letter does not appear in the word. Current wrong attempts left: " + str(attempts))

def win_or_lose(display_word, chosen_word):
    """Determines whether the player has won or lost."""
    if '_' not in display_word:
        print("Congratulations! You have correctly guessed the word!")
        print(' '.join(display_word))
        print("You survived!")
    else:
        print("Oh no! You have run out of attempts. Game Over!")
        print("The correct answer was: " + chosen_word)
        print("You Lost!")

if __name__ == "__main__":
    start_hangman_game()