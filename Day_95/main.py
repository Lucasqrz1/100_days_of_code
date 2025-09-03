import turtle
import math
import random

# Screen setup
wn = turtle.Screen()
wn.title("Space Invaders")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic screen updates

# Player
player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)
player_speed = 15

# Player bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.2, stretch_len=0.8)
bullet.penup()
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready"  # "ready" or "fire"

# Enemy
enemy_speed = 0.1
enemies = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-350, 260)
score_pen.write(f"Score: {score}", align="left", font=("Courier", 14, "normal"))

# Functions
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt((t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2)
    return distance < 20

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    wn.update()

    # Move enemies
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Change direction at edges
        if x > 380 or x < -380:
            enemy_speed *= -1
            for e in enemies:
                e.sety(e.ycor() - 40)

        # Check collision with player
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            wn.bye()
            break

        # Check collision with bullet
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.goto(x, y)
            score += 10
            score_pen.clear()
            score_pen.write(f"Score: {score}", align="left", font=("Courier", 14, "normal"))

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
    
    # Bullet goes off screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"
