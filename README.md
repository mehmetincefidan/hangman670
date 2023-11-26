# Hangman Game

## Description
This Python script implements a simple Hangman game. The user tries to guess a word randomly chosen from a predefined list. The game tracks the guessed letters, updates the guessed word, and manages the player's lives.

## Features
- Randomly selects a word from a list.
- Allows the player to guess a letter.
- Tracks the guessed letters and updates the word with correct guesses.
- Reduces the player's lives if the guess is incorrect.
- Provides feedback on the status of the game, including the word, guessed word, remaining lives, and guessed letters.

## Usage
1. Open your Python environment or editor.
2. Copy and paste the provided code into a Python file (e.g., `hangman.py`).
3. Run the script to start the Hangman game.
4. Follow the prompts to guess a letter and receive feedback on each guess.
5. The game continues until the word is guessed or the player runs out of lives.

## Example
```python
if __name__ == "__main__":
    word_list_example = ["apple", "banana", "orange", "strawberry", "mango"]
    hangman_game = Hangman(word_list_example)
    hangman_game.ask_for_input()

    # Print the updated state of the game
    print(f"Word to guess: {hangman_game.word}")
    print(f"Word guessed: {hangman_game.word_guessed}")
    print(f"Number of lives: {hangman_game.num_lives}")
    print(f"Number of unique letters: {hangman_game.num_letters}")
    print(f"List of guesses: {hangman_game.list_of_guesses}")
