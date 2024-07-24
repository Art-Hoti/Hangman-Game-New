import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._choose_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Unique letters
        self.list_of_guesses = []
    
    def _choose_word(self):
        return random.choice(self.word_list).lower()
    
    def _get_user_input(self):
        while True:
            guess = input("Please enter a single letter: ").strip().lower()
            if self._is_valid_guess(guess):
                return guess
            print("Invalid letter. Please enter a single alphabetical character.")
    
    def _is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses
    
    def _evaluate_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self._update_word_guessed(guess)
            self.num_letters -= self.word.count(guess)  # Unique letters
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)
    
    def _update_word_guessed(self, guess):
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess

    def ask_for_input(self):
        guess = self._get_user_input()
        self._evaluate_guess(guess)

    def display_word(self):
        print(" ".join(self.word_guessed))
    
    def is_game_over(self):
        return self.num_lives == 0 or self.num_letters == 0

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    print("Welcome to Hangman!")
    print("Guess the country name.")
    game.display_word()

    while True:
        if game.num_lives == 0:
            print('You lost!')
            print(f"The word was '{game.word}'.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            game.display_word()
        else:
            print('Congratulations. You won the game!')
            break

if __name__ == "__main__":
    word_list = ["United Kingdom", "Canada", "Australia", "New Zealand", "India"]
    play_game(word_list)
