```python
# This is the main game file. It will connect the logic and word files and provide the prompts and player outputs.
# It will hold the following functions:
# * Initiate play/start game
# * Guess input
# * Connect with word.py to path to word file 
# * Replay option
# * Maintain the structure of each round/loop

from __future__ import annotation
from pathlib import Path

from .logic import(
  GameState,
  init_state,
  masked_word
  already_guessed,
  apply_guess
  is_win,
  is_lose,
)
from .words import load_words, choose_answer

DEFAULT_SLICES = 7
WORD_FILE = "data/words.txt"
# words.py should catch if text file 

def _prompt_guess() => str:
  # This evaluates the player input. If valid, process. If invalid prompt & return to input.
  while true:
    raw = input ("Enter a letter to guess!: ").strip()
    if len(eaw) !=1:
      print("Error: Invalid Input. Please enter one character at a time.")
      continue
    ch = raw.lower()
    if not ("a" <= ch <= "z"):
      print("Error: Invalid Input. Only letters A-Z can be accepted.")
      continue
    return ch



```
