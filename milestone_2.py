import random

def choose_word(word_list):
    return random.choice(word_list)

def get_guess():
    while True:
        guess = input("Please enter a single letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Oops! That is not a valid input. Please enter a single alphabetical letter.")

def play_hangman(word):
    guessed_letters = set()
    attempts = 6
    while attempts > 0:
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word.lower())
        print(display_word)
        
        if '_' not in display_word:
            print("Congratulations! You guessed the word:", word)
            return True
        
        print("Attempts left:", attempts)
        guess = get_guess()
        
        if guess in guessed_letters:
            print("You've already guessed the letter", guess)
        elif guess in word.lower():
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print("Oops! Wrong guess.")
    
    print("Sorry, you ran out of attempts. The word was:", word)
    return False

def main():
    word_list = ["United Kingdom", "Canada", "Australia", "New Zealand", "India"]
    word = choose_word(word_list)
    print("Welcome to Hangman!")
    print("Guess the country name.")
    play_hangman(word)

if __name__ == "__main__":
    main()
