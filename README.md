# 🎮 Bouncy Breakout Game

## 📜 Description
![BreakoutGame](https://img.shields.io/badge/Breakout%20Game-Enhanced%20Version-blue) ![Python](https://img.shields.io/badge/Python-3.x-brightgreen)

The Enhanced Breakout Game is a classic arcade game where the player controls a paddle to bounce a ball and break a configuration of bricks. The game features a scoring system, colorful bricks, and a polished graphical interface.

### Features
- 🖼️ **Graphical Interface**: The game initializes a graphical window that includes bricks, a paddle, a ball, and score labels.
- 🖱️ **Mouse Control**: Players control the paddle using the mouse to bounce the ball.
- 🏆 **Scoring System**: Players earn points by breaking bricks.
- 🎮 **Game Over**: The game ends either when all the bricks are broken or the player loses all three lives.

## 🚀 Prerequisites
- Python 3.x
- The `campy` library

## 🎮 Usage

To run the game, navigate to the project directory and execute the following command:
```sh
python breakout.py
```

### 🎛️ User Configuration

You can customize the game settings by modifying the following variables in the `breakout.py` file:

- `FRAME_RATE`: Controls the speed of the game's frame rate.
  ```python
  FRAME_RATE = 10  # Default is 10 (100 frames per second)
  ```

- `NUM_LIVES`: Sets the number of lives the player starts with.
  ```python
  NUM_LIVES = 3  # Default is 3
  ```

## 📚 Gameplay Instructions

1. **Starting the Game**:
   - Click the graphical window to start the ball movement.

2. **Controlling the Paddle**:
   - Move the mouse to control the paddle's position.

3. **Objective**:
   - Break all the bricks to win the game.
   - Prevent the ball from falling out of the bottom of the screen.

4. **Scoring**:
   - Each brick broken gives 1 point.
   - The score is displayed at the bottom right of the window.

5. **Lives**:
   - The player starts with 3 lives (configurable).
   - The game ends when all lives are lost.

## 👨‍💻 Developer Information

If you're a developer looking to extend or modify the game, here are some key points to get you started:

- **BreakoutGraphics Class**: This class manages the graphical components and game logic. You can find it in the `breakoutgraphics.py` file.
- **Main Game Loop**: The main game loop is implemented in the `main` function within the `breakout.py` file.
- **Event Handling**: Mouse events are used to control the paddle and start the ball.


## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or improvements.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🧑‍💻 Author

- Cheryl Lin 我是雪兒 - [@Cheryl_Wei]
