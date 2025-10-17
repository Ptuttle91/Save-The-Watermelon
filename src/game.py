```python
# This is the main game file. It will connect the logic and word files and provide the prompts and player outputs.
# It will hold the following functions:
# * Initiate play/start game
# * Guess input
# * Connect with word.py to path to word file
# * Replay option
# * Maintain the structure of each round/loop

from __future__ import annotations
from pathlib import Path

from .logic import (
    GameState,
    init_state,
    masked_word,
    already_guessed,
    apply_guess,
    is_win,
    is_lose,
)
from .words import load_words, choose_answer

DEFAULT_SLICES = 7
WORD_FILE = "data/words.txt"
# words.py should catch if text file has any issues. If so, returns the default library.

def _prompt_guess() -> str:
    # This evaluates the player input. If valid, process. If invalid prompt & return to input.
    while true:
     raw = input("Enter a letter to guess!: ").strip()
     if len(raw) != 1:
        print("Error: Invalid Input. Please enter one character at a time.")
        continue
    ch = raw.lower()
    if not ("a" <= ch <= "z"):
        print("Error: Invalid Input. Only letters A-Z can be accepted.")
        continue
    return ch

def _prompt_replay() -> bool:
    # This is the prompt for to replay
    while true:
        raw = input("Would you like to play again? (y/n): ").strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Error: Invalid Input. Please enter 'y' or 'n'.")

def _words_source() -> list[str]:
    # This will load words from the designated file. Defaults to build-in word bank if fails.
    path = WORD_FILE if Path(WORD_FILE).exists() else None
    return load_words(path)

def play_round(slices: int = DEFAULT_SLICES) -> str:
    # This will draw the word ino the gamestate, and;
    # This will evaluate each round for a win or lose state.
    words = _words_sources()
    answer = choose_answer(words)
    state: GameState = init_state(answer, slices)

    while true:
        print(f"Secret Word:   {masked_word(state)}")
        print(f"Slices remaining: {state.slices}/{state.total_slices}")
        print("Guessed Letters:", ", ".join(sorted(state.guessed)) if state.guessed else " ")

    letter = _prompt_guess()

    if already_guessed(state, letter):
        # This will provide feedback for letters already guessed.
        print("' {letter} ' has already been guessed! Please try another")
        continue

    before = state.slices
    apply_guess(state, letter)
    after = state.slices

    if after == before and letter in state.answer:
        print(f"Well done! '{letter}' is a match!")
    elif after < before:
        print(f"Oh no! '{letter}' isn't in the word, they're getting closer to the watermelon!")

    if is_win(state):
        # This provides the output for a win state.
        print("Congratulations!")
        print("You are a hero to watermelons everywhere!")
        print(f"The Secret Word was: {state.answer}")
        print("Will you keep fighting?")

    if is_lose(state):
        # This provides the output for a lose state.
        print("Oh No!")
        print("The Watermelon has been SLICED!")
        print("The secret word was revealed in it's dying breath: {state.answer}!")
        print("No use in crying over spilled juice, will you keep fighting?")

def run() -> None:
    # This is the main loop with an introduction to start the game.
    print("Welcome, hero! The Watermelons need your help!")
    print("Guess the secret word to set them free!")
    while True:
        try:
            play_round(DEFAULT_SLICES)
        except Exception as ex:
            print(f"[Error] {ex}")
        if not _prompt_replay():
            print("Good job! Let's play again sometime!")
            break

if __name__ == "__main__":
    run()
```
