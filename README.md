# Save The Watermelon
## Readme File
CISC 179 Final Project
By: Patrick Tuttle

## Requirements:
* Windows 10 or later
* Python 3.10+ installed

## Getting Started:
* Download the Save the Watermelon game to your PC and extract the compressed files
* Open PowerShell and set it to the game directory.
*   Example: cd c:\[path]\Save-The-Watermelon-Main
* Once PowerShell is set to the active directory, run the game as a module by entering the following line:  py -m src.game
* You may now play the game!

## Game Rules:
* You may enter one letter at a time.
* You have seven tries to guess the letter correctly.
* If you've made seven guesses incorrectly, you've lost the game.
* If you guess all the correct letters, you've won!

## Making The Game Unique
* The word bank is stored in a customizable text file located in the /data folder.
* To modify the word bank, navigate to the words.txt file in the data folder.
*     Special Note: Do not modify the words.py file in the /src folder.
* Open the words.txt file and create or remove entries, with one word per line.
* Note: The game does not support non-alphabet characters, such as spaces, dashes, or numbers.
* To modify the quantity of slices, which act your lives (Or as we in the melon-mercenary industry refer to them as Slives) do the following:
*   Open the 'game.py' file within the /src directory using a Python compiler
*   Navigate to the DEFAULT_SLICES variable. Modifying the following number will change the amount of lives available.
