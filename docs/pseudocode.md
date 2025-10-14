# Pseudocode

* This must use the standard library only. To achieve this I am focusing on random, pathlib, and dataclasses.
* Input fuction must be simple and clean.
* The core parts of the game must be shown and updated after each attempt (slices, attempts, etc.)

## src/logic.py
### The core mechanics and data structuring of the system. No outputs

* I am using dataclass to keep this neat and lightweight.
* We will keep the logic.py file print free so it can be tested effectively without potential outlier errors.

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
## src/words.py

* Adding in a default list to help with testing.
* If word list not loaded, fall to default list.
* Using file loader.
* Using lowercase alphabet only.
* Strip blank lines.
* For stretch goal, move WordEntry(answer, hint) and parse these lines. Should not need more changes to fit.

```python
CONST DEFAULT_WORDS = [
    "snail", "watermelon", "cat", "banana", "wolverine", "orange", "badger", "grape", "antelope", "calamansi",
]

FUNCTION load_words(path: string | None) -> list[string]:
  IF path IS NOT None:
    IF File at path DOES NOT exist:
      RAISE FileNotFoundError("Error: Word file not found.")
    lines= read_all_lines_utf8(path)
    words = []
    FOR each line IN lines:
      w = strip(line)
      IF w IS empty OR starts with('#'): CONTINUE
      IF w.isalpha() AND w.islower():
        APPEND w to words
  ELSE:
    words = copy_of(DEFAULT_WORDS)
  IF words IS empty:
    RAISE ValueError("Error: No Valid Words Available.")
  RETURN words

FUNCTION choose_answer(words: list[string[, rng: Random | None) -> string:
  r = rng IF rng NOT None ELSE global_random
  RETURN r.choice(words)
```
## src/game.pt
### This will hold the loop to cycle through turns AND hold the input validation
* This should be the only section to print or read player input.
* UX - make sure already guessed letters are sorted and always displayed.
* UX - Heed spacing for visual clarity
* UX - Ensure that outcome of input is clearly stated and fun.
* Invalid input should re-prompt for input, not count as incorrect guess
* Duplicate guesses should not count as incorrect
* Define error is word import list is invalid
* Keep words/input processed as lowercase to keep streamline

```python
# These import the logic and word bank from the other sections of the program.
IMPORT from logic: init_state, masked_word, already_guessed, apply_guess, is_win, is_lose
IMPORT from words: load_words, choose_answer

# This declares constants for default value of slices
CONST DEFAULT_SLICES = 7

#change to = None to force switch to default library
CONST WORD_FILE = "data/words.txt"

# This structure creates and validate player input (a-z, length of input, etc.)
FUNCTION _prompt_guess() -> string:
  LOOP:
    raw = input("Enter a single letter to guess: ").strip()
    IF len(raw) != 1:
      print("Error: Invalid Input. Please enter one character at a time.")
      continue
    ch = to_lower(raw)
    IF ch NOT IN 'a'.. 'z':
      print("Error: Invalid Input. Only letters A-Z can be accepted.")
    RETURN ch

# These will build the function to replay after win or lose state
FUNCTION _prompt_replay() -> bool:
    LOOP:
        raw = input("Would you like to play again? (y/n): ").strip().lower()
        IF raw IN ["y","yes"]: RETURN True
        IF raw IN ["n","no"]:  RETURN False
        print("Error: Invalid Input. Please enter 'y' or 'n'.")

FUNCTION play_round(slices: int = DEFAULT_SLICES) -> string: 
    word_list = load_words(WORD_FILE)
    answer = choose_answer(word_list)
    state = init_state(answer, slices)

  # This is the print series that displays the title and the UI.
LOOP:
  print("")
  print("Save the Watermelon!")
  print(f"Secret Word: " + masked_word(state))
  print(f"Slices: {state.slices} out of {state.total_slices}")
  IF state.guessed IS empty:
    print("Guessed Letters: ")
  ELSE:
    print("Guessed Letters: " + join_sorted_by_comma(state.guessed))

    letter = _prompt_guess()

# This will be the input feedback for a correct/incorrect guess

# This will be the print series for a win state
# This will be the print series for a lose state

# This will print a Fun introduction to the game

# This will print a 'thank you' message if player does not want to continue

# Close up with:
IF__name__ == "__main__"
  run()
  ```
