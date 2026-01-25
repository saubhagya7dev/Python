import random

def get_random_word(word_list):
    """Selects a random word from a given list."""
    return random.choice(word_list).upper()

def display_current_progress(word, guessed_letters):
    """Displays the current progress of the word being guessed."""
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word_list = ["PYTHON", "DEVELOPER", "PROGRAMMING", "HANGMAN", "CODING", "COMPUTER","SAUBHAGYA","Harsh_Prabhakar"]
    selected_word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print("_ " * len(selected_word))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").upper()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in selected_word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        current_progress = display_current_progress(selected_word, guessed_letters)
        print("Current word: ", current_progress)
        
        if "_" not in current_progress:
            print("\nCongratulations! You've guessed the word correctly!")
            break
    else:
        print("\nSorry, you've run out of guesses. The word was:", selected_word)
    
    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    hangman()
