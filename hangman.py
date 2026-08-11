import random

def play_hangman():
    # 5 predefined words as per the requirement
    words = ["python", "programming", "codealpha", "internship", "developer"]
    secret_word = random.choice(words)
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print("Try to guess the secret word one letter at a time.")
    print(f"You can make up to {max_incorrect_guesses} incorrect guesses.")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        display_word = "".join([char if char in guessed_letters else "_" for char in secret_word])
        
        print("\n" + "="*30)
        print(f"Word to guess: {display_word}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters so far: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check for win condition
        if display_word == secret_word:
            print(f"\nCongratulations! You've guessed the word correctly: {secret_word}")
            break
            
        guess = input("Enter a letter: ").strip().lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid input. Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("\nYou already guessed that letter! Try a different one.")
            continue
            
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"\nIncorrect! '{guess}' is not in the word.")
        else:
            print(f"\nGood guess! '{guess}' is in the word.")
            
    if incorrect_guesses == max_incorrect_guesses:
        print("\n" + "="*30)
        print(f"Game Over! You've run out of incorrect guesses.")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
