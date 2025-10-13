# Design Document

## Problem Statement and Target Audience

The goal is to build a lightweight terminal-based word game. The player will 'Save the Watermelon' by guessing a secret word chosen from a hidden list. The goal is to make it fun, engaging, and replayable for short sessions. The target audience, in this scenario, will be my CISC 179 professor. 

## Game Rules & Win/Lose Conditions

~*~ The game will choose a 'secret' word at random from a list or category
~*~ The Game will display a masked version of the word to show counter of remaining 'Slices'
~*~ The Player will enter a single letter per turn; duplicates will not count
~*~ The player's correct guess will reveal all matching positions.
~*~ The player's incorrect guess will consume a 'slice'.
~*~ The player will win if they can guess all letters before the slices reach '0'
~*~ The player will lose if the slice counter reaches '0'. 

## Core Features

~*~ Random word selection. Can use an online dictionary to source words that fit difficulty criteria
~*~ Masked display that reveals correct guesses with progression
~*~ Input validation (standard alphabet, A-Z)


## Stretch Goals
Consider a 'Hard Mode' that: does not display the letters tried; more complex words
