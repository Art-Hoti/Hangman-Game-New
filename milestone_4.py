import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def main():
    word_list = ["united kingdom", "canada", "australia", "new zealand", "india"]
    hangman_game = Hangman(word_list)
    print("Welcome to Hangman!")
    print("Guess the country name.")
    
    while hangman_game.num_lives > 0 and hangman_game.num_letters > 0:
        print("Word guessed so far:", " ".join(hangman_game.word_guessed))
        hangman_game.ask_for_input()
    
    if hangman_game.num_lives == 0:
        print(f"Game over! The word was: {hangman_game.word}")
    else:
        print(f"Congratulations! You guessed the word: {hangman_game.word}")

if __name__ == "__main__":
    main()
