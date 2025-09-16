import random

def hangman():
    # Predefined list of words
    words = ["apple", "banana", "grapes", "orange", "mango"]
    
    # Randomly choose a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)  # underscores for unguessed letters
    guessed_letters = []  # store guessed letters
    attempts_left = 6

    print("🎮 Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    while attempts_left > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("❌ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            # Reveal correct letters
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts_left}")

        print("Word:", " ".join(guessed_word))
        print("Guessed letters:", ", ".join(guessed_letters))

    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)


# Run the game
hangman()
