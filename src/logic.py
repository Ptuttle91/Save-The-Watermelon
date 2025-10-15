```python

#This is the core game mechanics for 'Save the Watermelon'
#This module holds the logic, mainly the GameState information and its mutables.

from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class GameState:
  ## This is the container for all mutable game states.
  ## It holds the following attributes:
  #### - answer: The hidden word
  #### - correct_tries: A mask/unmasked with prepositioning for correctly guessed letters.
  #### - guessed: This is the bank of all letters that have been guessed
  #### - slices: The amount of remaining lives.
  #### - total_slices: The starting lives value, modify for potential difficulty adjustments.
  answer: str
  correct_tries: list[str]
  guessed: set[str] = field(default_factory=set)
  slices: int = 
  total_slices: int = 7

```
