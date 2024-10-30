"""
Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Breakout game where the player uses a paddle to bounce a ball
to break all the bricks. The player starts with 3 lives and must
prevent the ball from falling out of the bottom of the screen
using the paddle.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 12  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    """
    This program executes breakout game.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES  # 可調整

    # Add the animation loop here!
    while lives > 0:
        if graphics.is_ball_moving():  # 是ball_moving
            if not graphics.move_ball():  # If the ball falls outside, move_ball() returns False
                lives -= 1
                if lives > 0:
                    graphics.reset_game()
        if graphics.check_for_collisions():
            pass
        pause(FRAME_RATE)

        if graphics.bricks_remaining():
            graphics.write_texts("You Win!")
            graphics.window.remove(graphics.paddle)
            graphics.window.remove(graphics.ball)
            break

    if lives == 0:
        graphics.write_texts("Game Over")


if __name__ == '__main__':
    main()
