# Forest Adventure Game

This Python program creates a text-based adventure game where the user is stuck in a forest and interacts with an AI to navigate through various scenarios. The AI, powered by OpenAI's GPT-3.5 model, generates responses based on the user's input to create an engaging and challenging game experience. The game is designed to keep the player engaged with a series of intriguing scenarios that make it seem like they are progressing, but in reality, they are being led deeper into the forest.

Inspired by a certain episode of Rick & Morty, this game offers a unique blend of humor, challenge, and unpredictability.

## Features
- Engaging text-based gameplay with AI-generated content.
- Dynamic response generation that adapts to the player's input.
- Atmospheric theme music played throughout the game.
- Color-coded text for better user experience and immersion.

## Usage
To play the game, run the `forest_game` function in the `forest.py` file. The game will prompt the user for input and respond with AI-generated scenarios.

## Dependencies
- Python 3.x
- OpenAI Python library
- `playsound` library for playing theme music
- `threading` for concurrent execution of music playback
- `subprocess` and `sys` for cross-platform compatibility

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries: `openai`, `playsound`.
3. Run the `forest.py` file using a Python interpreter with the argument `run_game` to start the game.

## Additional Notes
- The game includes characters such as 'Big L' and 'Top G' as part of the storytelling.
- ANSI escape codes are used to colorize the user and AI inputs for better visualization.
- The game is designed to be run in a terminal or command-line interface.

Enjoy your adventure in the forest, and remember, not everything is as it seems!
