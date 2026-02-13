import random

# Predefined word list
words = ["python", "java", "excel", "sql", "github"]

# Random word select
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1:
        print("⚠ Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)
    else:
        print("✅ Good guess!")

# Lose condition
if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
