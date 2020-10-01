import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Sean Moore")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0) # stops window from updating automatically

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Speed of animation (max speed)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0) # Starts paddle a on left side in the middle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # Speed of animation (max speed)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup() # So the object does not draw straight up
paddle_b.goto(350, 0) # Starts paddle a right side in the middle

# Ball
ball = turtle.Turtle()
ball.speed(0) # Speed of animation (max speed)
ball.shape("square")
ball.color("white")
ball.penup() # So the object does not draw straight up
ball.goto(0, 0) # centers ball
ball.dx = 0.09 # ball movement speed 
ball.dy = 0.09

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # Hides pen, only need the text
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 20, "normal"))


# Function for keyboard inputs
def paddle_a_up():
    y = paddle_a.ycor() # returns y cordinate
    y += 40
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor() # returns y cordinate
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # returns y cordinate
    y += 40
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor() # returns y cordinate
    y -= 40
    paddle_b.sety(y)

# Keyboard binding
win.listen() # Tells program to listen for input
win.onkeypress(paddle_a_up, "w") # When "w" is pressed, move up

win.listen() # Tells program to listen for input
win.onkeypress(paddle_a_down, "s") # When "s" is pressed, move down

win.listen() # Tells program to listen for input
win.onkeypress(paddle_b_up, "Up") # When "up arrow" is pressed, move up 

win.listen() # Tells program to listen for input
win.onkeypress(paddle_b_down, "Down") # When "down arrow" is pressed, move down


#main game loop
while True:
    win.update() # every time loop runs it updates screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reversed direction once boarder is found
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reversed direction once boarder is found
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0, 0) # Centers ball
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0) # Centers ball
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 20, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

