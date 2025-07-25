import random

def hangman():
    # Predefined list of words
    word_list = ["python", "hangman", "simple", "coding", "github"]
    
    # Randomly choose a word
    chosen_word = random.choice(word_list)
    guessed_letters = []  # store guessed letters
    wrong_guesses = 0
    max_wrong = 6
    
    # Create a display version of the word (with _)
    display_word = ["_" for _ in chosen_word]
    
    print("🎮 Welcome to Hangman!")
    print("You have 6 chances. Good luck!\n")
    
    while wrong_guesses < max_wrong and "_" in display_word:
        print("Word: ", " ".join(display_word))
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        guess = input("Guess a letter: ").lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.\n")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue
        
        guessed_letters.append(guess)
        
        # Check guess
        if guess in chosen_word:
            print("✅ Good guess!\n")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!\n")
    
    # Game Over
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", chosen_word)
    else:
        print("💀 You ran out of guesses! The word was:", chosen_word)

# Run the game
if __name__ == "__main__":
    hangman()

