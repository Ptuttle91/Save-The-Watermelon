# Design Document

## Problem Statement and Target Audience

The goal is to build a lightweight terminal-based word game. The player will 'Save the Watermelon' by guessing a secret word chosen from a hidden list. The goal is to make it fun, engaging, and replayable for short sessions. The target audience, in this scenario, will be my CISC 179 professor. 

## Game Rules & Win/Lose Conditions

* The game will choose a 'secret' word at random from a list or category
* The Game will display a masked version of the word to show counter of remaining 'Slices'
* The Player will enter a single letter per turn; duplicates will not count
* The player's correct guess will reveal all matching positions.
* The player's incorrect guess will consume a 'slice'.
* The player will win if they can guess all letters before the slices reach '0'
* The player will lose if the slice counter reaches '0'. 

## Core Features

* Random word selection. Can use an online dictionary to source words that fit difficulty criteria
* Masked display that reveals correct guesses with progression
* Input validation (standard alphabet, A-Z)
* 'Slice Counter' that will update per turn (0/-1 based on guess)
* Track letters guessed. ASCII "letter bank" if time permits.
* A fun win/lose prompt, option to play again and raise or lower difficulty

## Stretch Goals
* An 'Intro' story with ASCII art; play once at start - NOT with 'play again', skipable with input.
* Consider a 'Hard Mode' that: does not display the letters tried; more complex words
* ASCII Art: Review existing sources of open use ascii art
* Hint system
* Categories
* 'Win streak' system per session; local file?
* ASCII form of the counter - A cat that inches close and closer to the melon with its claws outstretched! Stop him!

# Basic Flow
## Start
* Select game style
* Load bank of words
* Display 'ui'; masked word, slices, attempt bank

## Turn State
* Prompt the player to submit a letter; validate all input
* If guess is 'corect' (In the word), reveal its position in the 'mask'.
* If already tried, notify the user with a small prompt
* If guess is 'incorrect' (Not in the word), decrease 'slices' by 1.
* At end of each turn, check if win state (all letters guessed) OR lose state (out of slices)
* Else, continue to next turn.

## End Game State
* Reveal the Word
* Prompt to play again or exit the game

