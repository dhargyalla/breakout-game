from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_left(self):
        new_x = self.xcor() - 20
        if new_x > -280:  # Keep paddle within screen bounds
            self.goto(new_x, self.ycor())  # Move only if within bounds

    def move_right(self):
        new_x = self.xcor() + 20
        if new_x < 280:
            self.goto(new_x, self.ycor())
