from turtle import Turtle

# Constants for brick placement
BRICK_START_X = -230
BRICK_START_Y = 250
BRICK_GAP = 50
ROWS = 5
COLS = 10

class Bricks:
    def __init__(self):
        self.bricks = []  # Store all bricks here

    def create_bricks(self):
        for row in range(ROWS):
            for col in range(COLS):
                brick_x = BRICK_START_X + col * BRICK_GAP
                brick_y = BRICK_START_Y - row * BRICK_GAP / 2
                brick = Brick((brick_x, brick_y))
                self.bricks.append(brick)
        return self.bricks

class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)
