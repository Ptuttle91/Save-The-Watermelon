### This file contains:
### * A default word bank.
### * Defines function for loading a new word bank.
### * Defines a function to select a random word from the bank.

from __future__ import annotations
import random
from pathlib import Path

_DEFAULT_WORDS: list[str] = [
  "snail", "watermelon", "cat", "banana", "wolverine", "orange", "badger", "grape", "antelope", "calamansi", "rat", "tangerine",
]

def load_words (path: str | None = None) -> list[str]:
  # This loads words from a .txt file if indicated.
  # If no data file is provided, the function will fall to default word bank.
  # Data is sanitized to only accept alphabetic characters in lower case.
  words: list[str] = []
  if path:
    p = Path(path)
    if p.exists():
          for line in p.read_text(encoding="etf-8").splitlines():
            w = line.strip()
            if not w or w.startswith("#"):
              continue
            if w.isalpha() and w.islower():
              words.append(w)
  if not words:
    words = list(_DEFAULT_WORDS)
  return words

def choose_answer(words: list[str], rng: random.Random | None = None) ->str:
  #This function will pick a word randomly from the word bank.
  r = rng or random
  return r.choice(words)
