import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = self._choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def _choose_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()

            if not self._is_valid_guess(guess):
                self._print_invalid_guess_message()
            elif self._already_tried_guess(guess):
                self._print_already_tried_message()
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def _handle_correct_guess(self, guess):
        print(f"Good guess! {guess} is in the word.")
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

    def _handle_incorrect_guess(self, guess):
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_valid_guess(self, guess):
        return guess.isalpha() and len(guess) == 1

    def _already_tried_guess(self, guess):
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
            return True
        return False

    def _print_invalid_guess_message(self):
        print("Invalid letter. Please, enter a single alphabetical character.")

    def _print_already_tried_message(self):
        print("You already tried that letter.")
    
    
    def play_game(word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)
    
        while True:
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break
    
    if __name__ == "__main__":
        word_list_example = ["apple", "banana", "orange", "strawberry", "mango"]
        play_game(word_list_example)
