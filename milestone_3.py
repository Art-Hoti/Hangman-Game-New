import random

def choose_word(word_list):
    return random.choice(word_list).lower()

def get_guess():
    while True:
        guess = input("Please enter a single letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

def check_guess(guess, word, guessed_letters):
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
    elif guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        guessed_letters.add(guess)
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        guessed_letters.add(guess)

def display_word(word, guessed_letters):
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append('_')
    return ' '.join(display)

def main():
    word_list = ["United Kingdom", "Canada", "Australia", "New Zealand", "India"]
    word = choose_word(word_list)
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    print("Guess the country name.")
    
    while True:
        print("\nWord to guess:", display_word(word, guessed_letters))
        guess = get_guess()
        check_guess(guess, word, guessed_letters)
        
        # Check if all letters have been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word correctly:", word)
            break

if __name__ == "__main__":
    main()
