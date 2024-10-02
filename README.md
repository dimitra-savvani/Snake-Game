# Snake Game - README

## Introduction

This project is an implementation of the classic "Snake Game" using Python's `turtle` graphics library. The player controls the snake, trying to eat food to grow in length while avoiding collisions with the walls or the snake's own body. The game tracks and displays the current score, and saves the highest score in a local file.

## Project Structure

The project consists of four Python files:

- `main.py`: The main file initializes the game window, handles user input, and runs the game loop.
- `snake.py`: Contains the `Snake` class, which defines the snake's behavior, movement, and interactions.
- `food.py`: Contains the `Food` class, which generates and repositions the food for the snake to eat.
- `scoreboard.py`: Contains the `Scoreboard` class, which manages the score display and high score tracking.

## Dependencies

- Python 3.x
- `turtle` library (bundled with Python's standard library)

## How to Run

1. Ensure that Python 3 is installed on your system.
2. Download or clone the repository.
3. Run the game using the command:

```bash
python main.py
```
Make sure all the required files are in the same directory.

## Game Controls
- **Up Arrow**:** Move the snake up.
- **Down Arrow:** Move the snake down.
- **Left Arrow:** Move the snake left.
- **Right Arrow:** Move the snake right.

The game will restart automatically after a collision with the wall or the snake's body.

## File Descriptions
`main.py`

This file sets up the game window and handles the main game loop. It creates instances of the `Snake`, `Food`, and `Scoreboard` classes and listens for user input to control the snake's direction.

Key sections:

- Initializes the screen with a black background and the title "Snake Game".
- Binds the arrow keys to control the snake's movement.
- Runs the main game loop, where the snake moves continuously, checks for collisions with the walls or itself, and eats food to grow.
- On game-over, the snake and scoreboard are reset.

`snake.py`

This file defines the `Snake` class, which handles:

- Movement: Moves the snake in the current direction, with each body part following the one ahead.
- Growth: Grows the snake's tail each time it eats food.
- Collision Detection: Detects collisions with the walls or the snake's own body.
- Resetting: Resets the snake's position and size when the game is restarted.

`food.py`
 
This file defines the `Food` class, which:

- Generates a food item to a random position within the screen's limits.
- Repositions the food to a new random location when the snake eats it.

`scoreboard.py`

This file defines the `Scoreboard` class, which:

- Displays the current score and high score on the screen.
- Updates the score each time the snake eats food.
- Resets the score when the game is over, and updates the high score if necessary.
- Reads and writes the high score to a file called highscore.json.

## High Score

The game saves the high score in a `highscore.json` file. This file is read when the game starts, and the high score is updated if a new high score is achieved.

### Example `highscore.json`
```json
42
```
This JSON file contains the integer value of the highest score recorded.

## Customization
- Game Speed: The game speed can be adjusted by modifying the `time.sleep(0.1)` in the main game loop.
- Screen Size: Window size is set to 800x800 pixels by default. You can modify it by changing the `sc.setup(width=800, height=800)` line in `main.py`.
- Snake Color: The snake's color is set to white. You can change this in the `snake.py` file where each turtle object is created with `self.snake_body[-1].color('white')`.

## Future Enhancements
- Adding sound effects for eating food and colliding.
- Implementing different levels with increasing difficulty.
- Allowing the player to pause and resume the game.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
