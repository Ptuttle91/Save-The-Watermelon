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

def _project_data_words_path() -> Path:
  # This will direct the words.py file to the text document.
  return Path(__file__).resolve().parents[1] / "data" / "words.txt"

def _load_from_file(p: Path) -> list[str]:
  # This will read and validate the word bank from the file.
  if not p.exists():
    return []
 
  text = p.read_text(encoding="utf-8", errors="ignore")
  words: list[str] = []
  for line in text.splitlines():
    w = line.strip()
    if not w or w.startswith("#"):
      continue
    if w.isalpha() and w.islower():
       words.append(w)
  return words


def load_words (path: str | None = None) -> list[str]:
  # Loads words from .txt file
  # If no data file is provided, the function will fall to default word bank.
  if path:
      words = _load_from_file(Path(path))
        if words:
            return words
    auto = _project_data_words_path()
    words = _load_from_file(auto)
    if words:
        return words
    return list(_DEFAULT_WORDS)

def choose_answer(words: list[str], rng: random.Random | None = None) ->str:
  #This function will pick a word randomly from the word bank.
  r = rng or random
  return r.choice(words)
