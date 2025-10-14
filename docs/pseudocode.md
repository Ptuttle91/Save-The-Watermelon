# src/words.py
## Word list and loading them into the game
```python
import random
from pathlib import path

#create sample text for now, create dictionary for complete edition
_default_words = [
  "snail", "watermelon", "cat", "banana", "wolverine", "orange", "badger", "grape", "antelope", "calamansi",
]

def load_words(path: str | None = None) -> list[str]:
  """
  Import list of words from a file. Otherwise utilize the default words. Only keep lowercase words, with no numerals.
  if path:
    p=Path(path)
    if not p.exists():
      raise FileError(f"Error: An Appropriate Word File is not found at: {path}")
    words = [w.strip() for w in p.read_text(encoding="utf-8").splitlines()]
  else:
    words = list(_default_words)
  words = [w for w in words if w.isalpha() and w.islower()]
  if not in words
    raise ValueError("Error: No Valid Words Available.")

def choose_answer(words: list[str], rng: random.Random | None = None) -> str:
  r = rng or random
  return r.choice(words)
```
# src/logic.py
## The core mechanics
```python

@dataclass
class GameState:
  answer:str
  correct_tries: list[str]
  guessed: set[str] = field(default_factory=set)
  slices: int = 7
  total_slices: int = 7

def init_state(answer: str, slices: int = 7) = GameState
  mask = ["_"] * len(answer)
  return Gamestate(answer=answer, correct_tries=mask, slices=slices, total_slices=slices)

def masked_word(state: GameState) -> str:
  return " ".join(state.correct_tries)

def already_guessed(state:GameState, letter: str) - ) bool:
  return letter in state.guessed

def apply_guess(state:GameState, letter: str) -> None:
  if letter in state.guessed:
    reutrn
  state.guessed.add(letter)
  if letter in state.answer:
    for i, ch in enumerate(state.answer)
      state.correct_tries[i] = letter
  else:
    state.slices -= 1

def is_win (state:GameState) -> bool:
  return "_" not in state.correct_tries

def is_lose(state: GameState) -> bool:
  return state.slices <= 0
```

# src /game.py
## UI/ux portion, prompts, input validation

```python
from .logic import (
  GameState, init_state, masked_word, already_guessed, apply_guess, is_win, is_lose
)
from .words import load_words, choose_answer

default_slices = 7
word_file = "data/words.txt" # can change to 'None' if we want to use default/test dictionary

def _prompt_guess() ->
  while True:
    raw = input ("Please enter a single letter (A through Z): ").strip()
    if len(raw) !=1:
      print("Error: Invalid Input. Please enter one letter at a time.")
      continue
    ch = raw.lower()
    if not ("a" <= ch <="z"):
      print("Error: Please enter a valid letter from the alphabet. A-Z only.)
      continue
    return ch

def _prompt_replay() -> bool:
  while True:
    raw = input ("Play Again? (y/n): ").strip().lower()
    if raw in ("y", "yes"): return True
    if raw in ("n", "no"): return False
    Print("Error: Please enter a valid input: Y or N.")

def play_turn(slices: int = DEFAULT_SLICES) -> str:
  words = load_words(word_file) # note: Can use load_words(none) to use default list in testing.
  ans = choose_answer(words)
  state: GameState = init_state(ans, slices)

  while True:
    print("\nSave the Watermelon!!")
    print(f"Word: {masked_word(state)}")



