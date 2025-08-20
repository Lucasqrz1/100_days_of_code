import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)  # Turns off animation for smoother gameplay

# Create the paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)  # Make it wider
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -200)
ball_dx = 2.0  # Ball speed in x direction
ball_dy = 2.0  # Ball speed in y direction

# Create bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

# Create 5 rows of bricks with different colors
for row in range(5):
    for col in range(10):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        # Position bricks in a grid
        x = -180 + (col * 40)  # 40 units apart horizontally
        y = 200 - (row * 30)   # 30 units apart vertically
        brick.goto(x, y)
        bricks.append(brick)

# Score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 250)

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# Paddle movement functions
def paddle_left():
    x = paddle.xcor()
    if x > -350:  # Don't let paddle go off screen
        paddle.setx(x - 20)

def paddle_right():
    x = paddle.xcor()
    if x < 350:   # Don't let paddle go off screen
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(paddle_left, "Left")
screen.onkey(paddle_right, "Right")
screen.onkey(paddle_left, "a")
screen.onkey(paddle_right, "d")

# Game loop
update_score()

while True:
    screen.update()
    time.sleep(0.01)  # Small delay to control game speed
    
    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    
    # Ball collision with walls
    if ball.xcor() > 390:  # Right wall
        ball_dx *= -1
    
    if ball.xcor() < -390:  # Left wall
        ball_dx *= -1
    
    if ball.ycor() > 290:  # Top wall
        ball_dy *= -1
    
    # Ball collision with paddle
    if (ball.ycor() > -260 and ball.ycor() < -240 and 
        ball.xcor() > paddle.xcor() - 50 and 
        ball.xcor() < paddle.xcor() + 50):
        ball_dy *= -1
        
        # Add some angle based on where ball hits paddle
        hit_position = (ball.xcor() - paddle.xcor()) / 50
        ball_dx += hit_position * 0.1
    
    # Ball goes below paddle (game over condition)
    if ball.ycor() < -290:
        # Reset ball position
        ball.goto(0, -200)
        ball_dx = 2.0
        ball_dy = 2.0
        # You could add lives/game over logic here
    
    # Ball collision with bricks
    for brick in bricks[:]:  # Use slice to avoid modifying list during iteration
        if (ball.xcor() > brick.xcor() - 20 and 
            ball.xcor() < brick.xcor() + 20 and
            ball.ycor() > brick.ycor() - 10 and 
            ball.ycor() < brick.ycor() + 10):
            
            # Remove the brick
            brick.hideturtle()
            bricks.remove(brick)
            
            # Reverse ball direction
            ball_dy *= -1
            
            # Increase score
            score += 10
            update_score()
            
            # Speed up ball slightly
            if abs(ball_dx) < 0.5:
                ball_dx *= 1.02
            if abs(ball_dy) < 0.5:
                ball_dy *= 1.02
            
            break  # Only hit one brick per frame
    
    # Check win condition
    if len(bricks) == 0:
        # Display win message
        win_text = turtle.Turtle()
        win_text.color("green")
        win_text.penup()
        win_text.hideturtle()
        win_text.goto(-100, 0)
        win_text.write("YOU WIN!", font=("Arial", 24, "bold"))
        break

# Keep window open
screen.exitonclick()