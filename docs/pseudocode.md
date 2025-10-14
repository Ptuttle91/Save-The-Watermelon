# Pseudocode

* This must use the standard library only. To achieve this I am focusing on random, pathlib, and dataclasses.
* We will keep the logic.py file print free so it can be tested effectively without potential outlier errors.
* Input fuction must be simple and clean.
* The core parts of the game must be shown and updated after each attempt (slices, attempts, etc.)

## src/logic.py
### The core mechanics and data structuring of the system. No outputs

I am using dataclass to keep this neat and lightweight.

```python

DATASTRUCT GameState:
  # The word, all lower case
  answer: string
  # The system used for masking and revealing letters
  correct_tries:list[string]
  # The letters player has already attempted
  guessed: set[string]
  # The amount of 'slices' left
  slices: int
  # The maximum value of 'slices' used in the ui.
  total_slices: int

FUNCTION init_state(answer: string, slices: int) -> GameState:
  mask=['_'] * len(answer)
  RETURN GameState(
        answer=answer,
        correct_tries=mask,
        guessed=empty set,
        slices=slices,
        total_slices=slices
    )

# A helper built for the display. Applies an underscore per length of answer.
Function masked_word(state:GameState) -> string:
  RETURN join_with_spaces(state.correct_tries)

# This checks input for duplicate attempts
FUNCTION already_guessed(state: GameState, letter: string) -> bool:
    RETURN letter IN state.guessed

# This helps set the true/false/duplicate status for the input attempts
FUNCTION apply_guess(state: GameState, letter: string) -> None:
  # This stops a duplicate entry from costing a slice
  IF letter IN state.guessed:
    RETURN
  # This adds guessed letter to the word bank
  ADD letter TO state.guessed
  # This reveals the correctly guessed letters
  IF letter IN state.answer:
    for i FROM 0 to len(state.answer)-1:
      if state.answer[i] == letter:
        state.corred_tries[i] = letter
  #This subtracts a slice for an incorrect guess.
  ELSE:
    state.slices = state.slices -1

# This calls a win-state if _ are all cleared out
FUNCTION is_win(state: GameState)-> bool:
  RETURN '_' NOT IN state.correct_tries

# This calls a lose-state when slices = 0
FUNCTION is_lose (state: GameState) -> bool:
  RETURN state.slices <=0

```

