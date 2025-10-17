#Logic Test file

import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import unittest

from logic import (
    init_state,
    masked_word,
    already_guessed,
    apply_guess,
    is_win,
    is_lose,
)

from word import load_words

class TestLogic(unittest.TestCase):
    def test_init_sets_mask_and_slices(self):
        # This will test the masking function to hide answer.
        gs = init_state("grape", 7)
        self.assertEqual(masked_word(gs), "_ _ _ _ _")
        self.assertEqual(gs.slices, 7)
        self.assertEqual(gs.total_slices, 7)
        self.assertEqual(gs.guessed, set())

    def test_correct_guess_reveals_all_matches(self):
        # This will test that correct input with replace the mask in all spaces.
        gs = init_state("banana", 7)
        apply_guess(gs, "a")
        self.assertEqual(masked_word(gs), "_ a _ a _ a")
        self.assertEqual(gs.slices, 7)

    def test_miss_costs_one_slice(self):
        # This function will test to ensure that slices are removed when input is incorrect.
        gs = init_state("grape", 7)
        apply_guess(gs, "z")
        self.assertEqual(gs.slices, 6)

    def test_duplicate_guess_no_penalty(self):
        # This will ensure that duplicate guesses are not counted as incorrect.
        gs = init_state("grape", 7)
        apply_guess(gs, "z")
        apply_guess(gs, "z")
        self.assertEqual(gs.slices, 6)

    def test_already_guessed(self):
        # This will ensure that the round continues following duplicated inputs.
        gs = init_state("pear", 7)
        apply_guess(gs, "p")
        self.assertTrue(already_guessed(gs, "p"))
        self.assertFalse(already_guessed(gs, "x"))

    def test_win_condition(self):
        # This will verify that the 'win' state logic triggers correctly.
        gs = init_state("aa", 3)
        apply_guess(gs, "a")
        self.assertTrue(is_win(gs))
        self.assertFalse(is_lose(gs))

    def test_lose_condition(self):
        # This will verify that the 'lose' state logic triggers correctly.
        gs = init_state("a", 1)
        apply_guess(gs, "z")
        self.assertTrue(is_lose(gs))
        self.assertFalse(is_win(gs))


class TestWords(unittest.TestCase):
    def test_load_words_default_contains_bank(self):
        # This checks that the default work bank loads correctly.
        words = load_words(None)
        required = {
            "snail", "watermelon", "cat", "banana", "wolverine", "orange",
            "badger", "grape", "antelope", "calamansi", "rat", "tangerine",
        }
        self.assertTrue(required.issubset(set(words)))
        self.assertTrue(all(w.islower() and w.isalpha() for w in words))

if __name__ == "__main__":
    unittest.main()
