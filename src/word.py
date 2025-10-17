### This file contains:
### * A default word bank.
### * Defines function for loading a new word bank.
### * Defines a function to select a random word from the bank.

```python
__from__ future import annotations
import random
from pathlib import Path

_DEFAULT_WORDS: list[str] = [ # put default list here, each word in quotes & separated by comma

]

def load_words (path: str | None = None) -> list[str]:
  # This loads words from a .txt file if indicated.
  # If no data file is provided, the function will fall to default word bank.
  # Data is sanitized to only accept alphabetic characters in lower case.
  

```
