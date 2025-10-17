#This is the core game logic for 'Save the Watermelon'
#This module holds the GameState and its mutables.

from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class GameState:
# This is the container for all mutable game states.
# It holds the following attributes:
# - answer: The hidden word
# - correct_tries: A mask/unmasked with prepositioning for correctly guessed letters.
# - guessed: This is the bank of all letters that have been guessed
# - slices: The amount of remaining lives.
# - total_slices: The starting lives value, modify for potential difficulty adjustments. Based on 'slices'.
    answer: str
    correct_tries: list[str]
    guessed: set[str] = field(default_factory=set)
    slices: int = 7
    total_slices: int = 7

def init_state(answer: str, slices: int = 7) -> GameState:
  ## This will initialize a new 'GameState' with the masked secret word
  mask = ["_"] * len(answer)
  return GameState(answer=answer, correct_tries=mask, slices=slices, total_slices=slices)

def masked_word(state: GameState) -> str:
  # This represents the masked word with correctly guessed letters.
  return " ".join(state.correct_tries)

def already_guessed(state: GameState, letter: str) -> bool:
    #This checks for duplicate guesses
    return letter in state.guessed


def apply_guess(state: GameState, letter: str) -> None:
  # This applies the guessed letter to the secret word, and handles accounting to correct/duplicate/wrong
    if letter in state.guessed:
        return
    state.guessed.add(letter)
    if letter in state.answer:
        for i, ch in enumerate(state.answer):
            if ch == letter:
                state.correct_tries[i] = letter
    else:
        state.slices -= 1

def is_win(state: GameState) -> bool:
  # This declares the game as won if it no longer detects an underscore in the variable for the random word.
  return "_" not in state.correct_tries

def is_lose(state: GameState) -> bool:
  # This declares the game as lost if the active slice/incorrect guess counter reaches 0 or less.
  return state.slices <=0
