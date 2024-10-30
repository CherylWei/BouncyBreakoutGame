"""
Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

The game initializes a graphical window with bricks, a paddle, a ball, and a score label.
Players control the paddle using the mouse to bounce the ball and break bricks, earning
points in the process. The game ends either when all bricks are broken or the player loses all lives.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.ball_radius = BALL_RADIUS
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = '#3b6fba'
        self.window.add(self.paddle, x=(self.window_width - paddle_width) / 2, y=self.window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = '#3b6fba'
        self.window.add(self.ball, x=self.window_width / 2 - ball_radius, y=self.window_height / 2 - ball_radius)
        self.ball_moving = False  # 開關

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmouseclicked(self.start_ball)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.initial_bricks = brick_rows * brick_cols
        self.remaining_bricks_count = self.initial_bricks
        color = None
        for i in range(brick_rows):
            for j in range(brick_cols):
                # 每個新brick的 x 座標
                x = j * (brick_width + brick_spacing)
                # 每個新brick的 y 座標
                y = i * (brick_height + brick_spacing)

                # 每兩行分一個組
                if i // 2 == 0:
                    color = '#f4c7c3'
                elif i // 2 == 1:
                    color = '#fce8b2'
                elif i // 2 == 2:
                    color = '#b7e1cd'
                elif i // 2 == 3:
                    color = '#c6dafc'
                elif i // 2 == 4:
                    color = '#e1bee7'

                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.window.add(self.brick, x=x, y=y)

        # Draw Score Label and Introduction
        self.score = 0
        self.score_label = GLabel(f'Score: {self.score}')
        self.score_label.font = '-30'
        self.window.add(self.score_label, x=self.window.width - 130, y=self.window.height - 5)

        self.welcome = GLabel('Welcome to Breakout!')
        self.welcome.font = '-30'
        self.welcome.color = 'magenta'
        self.window.add(self.welcome, x=self.window_width / 2 - self.welcome.width / 2, y=self.window_height - 380)

        self.intro_label = GLabel(
            '\nGuide to Playing the Game:'
            '\n1. Collect points by hitting the bricks with the ball'
            '\n2. Each Brick gives 1 point'
            '\n3. Move your paddle using the mouse'
            '\n4. Lives: You have 3 lives to start with'
            '\n5. Winning the Game: Break out all bricks'
            '\nClick to Start!')
        self.intro_label.font = '-15'
        self.window.add(self.intro_label, x=self.window.width / 2 - 160, y=self.window.height - 150)

        self.click_label = GLabel('Click to Start!')
        self.click_label.font = '-30'
        self.click_label.color = 'magenta'
        self.window.add(self.click_label, x=self.window_width / 2 - self.click_label.width / 2,
                        y=self.window_height - 100)

    def paddle_move(self, mouse):
        """
        This function has the paddle move with its center following the mouse.
        :param mouse: the mouse event.
        :return: None
        """
        self.paddle.x = mouse.x - self.paddle.width / 2
        if mouse.x - self.paddle.width / 2 <= 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width / 2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def start_ball(self, mouse):  # mouse trigger
        self.window.remove(self.welcome)
        self.window.remove(self.click_label)
        self.window.remove(self.intro_label)

        if not self.ball_moving:
            pause(500)
            self.__dy = INITIAL_Y_SPEED
            self.ball_moving = True  # avoid mouse events when running
            if self.__dx == 0:
                self.__dx = random.randint(1, MAX_X_SPEED)
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx

        if self.ball.y + BALL_RADIUS * 2 > self.window.height:
            self.reset_game()
            return False
        return True  # ball still in motion

    def check_for_collisions(self):
        # Top-left corner
        if self.when_collide(self.ball.x, self.ball.y):
            return True  # True if any collision
        elif self.when_collide(self.ball.x + self.ball.width, self.ball.y):
            return True
        elif self.when_collide(self.ball.x, self.ball.y + self.ball.height):
            return True
        elif self.when_collide(self.ball.x + self.ball.width, self.ball.y + self.ball.height):
            return True
        return False

    def when_collide(self, x, y):
        """
        Detects whether the ball hits the paddle or any bricks.
        :return: None, This function uses return to end the loops.
        """
        obj = self.window.get_object_at(x, y)
        if obj is not None:  # is obj（paddle or brick）
            if obj is self.paddle:
                self.__dy = -self.__dy
                self.ball.y = self.paddle.y - self.ball.height - 1
            elif obj is not self.ball and obj is not self.score_label:
                self.window.remove(obj)
                self.__dy = -self.__dy
                self.remaining_bricks_count -= 1
                self.score += 1
                self.score_label.text = f'Score: {self.score}'
                print(self.remaining_bricks_count)
            return True  # collide
        return False  # not obj

    def is_ball_moving(self):
        return self.ball_moving

    def reset_game(self):
        """
        This function resets the ball to its original position.
        :return: None
        """
        self.ball.x = self.window_width / 2 - BALL_RADIUS
        self.ball.y = self.window_height / 2 - BALL_RADIUS
        self.ball_moving = False
        self.__dx = 0
        self.__dy = 0

    def write_texts(self, message):
        text = GLabel(message)
        text.font = "-50"
        text.color = 'red'
        self.window.add(text, x=self.window.width // 2 - text.width // 2,
                        y=self.window.height // 2 - 30)

    def bricks_remaining(self):
        return self.remaining_bricks_count == 0

    def get_dx(self):
        """
        Getter of dx.
        :return self.__dx: the value of private variable dx.
        """
        return self.__dx

    def get_dy(self):
        """
        Getter of dy.
        :return self.__dy: the value of private variable dy.
        """
        return self.__dy

    def set_dx(self, new_dx):
        """
        Setter function to update dx and bounce the ball.
        :param new_dx: the new dx value passed from the server side to the coder side.
        :return: None, this function does not return anything.
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        Setter function to update dy and bounce the ball.
        :param new_dy: the new dy value passed from the server side to the coder side.
        :return: None, this function does not return anything.
        """
        self.__dy = new_dy
