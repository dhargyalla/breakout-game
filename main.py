from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time


# Screen configuration
screen = Screen()
text_turtle = Turtle()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Breakout game')

# Paddle configuration
paddle = Paddle((0, -250))
ball = Ball((0, -200))

# Instantiate the Bricks class and create the bricks
brick_manager = Bricks()
bricks = brick_manager.create_bricks()  # Creates and returns a list of
# Paddle movement bindings
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

# Function to reset the game
def reset_game():
    global bricks
    ball.reset_position()  # Reset ball position
    paddle.goto(0, -250)  # Reset paddle position
    # Clear existing bricks
    for brick in bricks:
        brick.hideturtle()
    bricks = brick_manager.create_bricks()  # Recreate bricks
    text_turtle.clear()  # Clear Game Over text

# Function to ask for restarting the game
def restart_prompt():
    screen.update()
    time.sleep(1)
    text_turtle.goto(0, 0)
    text_turtle.write("Play again? Press Y or N", align="center", font=("Arial", 24, "normal"))
    screen.update()
    screen.onkeypress(restart_game, "y")
    screen.onkeypress(exit_game, "n")

def exit_game():
    text_turtle.clear()
    screen.bye()

def restart_game():
    text_turtle.clear()
    reset_game()
    game_loop()

# Main game loop
def game_loop():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()  # Manually update the screen to reflect changes
        ball.move()

        # Ball collision with walls
        if ball.xcor() > 290 or ball.xcor() < -290:
            ball.bounce_x()
        if ball.ycor()>290:
            ball.bounce_y()

        # Ball hits the paddle
        if ball.distance(paddle) < 50 and ball.ycor() < -240:
            ball.bounce_y()

        # Ball collision with bricks
        for brick in bricks:
            if ball.distance(brick) < 30:
                ball.bounce_y()
                brick.hideturtle() # Hide the brick when hit
                bricks.remove(brick) # Remove the brick from the list

        # Game over if the ball hits the bottom wall
        if ball.ycor() < -290:
            ball.goto(0, -250)
            ball.write("Game Over!", align="center", font=("Arial", 24, "normal"))
            screen.update()  # Update the screen to display "Game Over"

            time.sleep(0.1)  # Give some delay to show the "Game Over" message
            ball.reset_position()  # Reset the ball position
            game_is_on = False  # End the game loop
            restart_prompt()  # Ask to restart the game

game_loop()
screen.mainloop()