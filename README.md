# Number Guessing Game

A simple command-line number guessing game written in Python where players try to guess a randomly generated number between 1 and 100.

This is one of the exercises at roadmap.sh   
[Link to the project](https://roadmap.sh/projects/number-guessing-game)

## Features

- Three difficulty levels:
  - Easy: 10 chances to guess
  - Medium: 5 chances
  - Hard: 3 chances
- Time tracking for each game session
- Highscore system that persists between games
- Input validation and error handling
- Helpful feedback after each guess

## Requirements

- Python 3.x
- No additional external packages required

## Installation

1. Clone or download this repository to your local machine
2. Navigate to the game directory
3. Run the game using Python:
```bash
python game.py
```

## How to Play

1. Launch the game
2. Select a difficulty level (1-3)
3. Enter your guess (a number between 1-100)
4. The game will tell you if your guess is too high or too low
5. Continue guessing until you find the correct number or run out of chances
6. Choose whether to play again

## Highscores

The game automatically tracks the best scores (lowest number of attempts) for each difficulty level. Highscores are saved in a `highscore.json` file and persist between gaming sessions.

## File Structure

- `game.py`: Main game script
- `highscore.json`: Stores the best scores for each difficulty level

## Error Handling

The game includes error handling for:
- Invalid difficulty selection
- Non-numeric inputs
- Corrupted highscore file