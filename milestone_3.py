import random

def choose_random_word(word_list):
    return random.choice(word_list).lower()

def get_valid_letter_guess():
    while True:
        guess = input("Please enter a single letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single alphabetical character.")

def check_letter_in_word(guess, word):
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def main():
    word_list = ["United Kingdom", "Canada", "Australia", "New Zealand", "India"]
    secret_word = choose_random_word(word_list)
    print("Welcome to Hangman!")
    print("Guess the country name.")

    while True:
        guess = get_valid_letter_guess()
        check_letter_in_word(guess, secret_word)

if __name__ == "__main__":
    main()
