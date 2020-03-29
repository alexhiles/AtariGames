import turtle
import os

wn = turtle.Screen()

wn.title("Pong by Alex Hiles")
wn.bgcolor("black")

disp_width  = 900
disp_height = 700

wn.setup(width=disp_width, height=disp_height)
wn.tracer(0) # stops window from updating

# Score
score_a = 0
score_b = 0

class Paddle:
    def __init__(self, shape, color,xcoord, ycoord, stretchx = 5, stretchy = 1):
        self.shape                   = shape
        self.color                   = color
        self.stretchx, self.stretchy = stretchx, stretchy
        self.xcoord, self.ycoord     = xcoord, ycoord

    def __call__(self):
        self.paddle         = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape(self.shape)
        self.paddle.color(self.color)
        self.paddle.shapesize(stretch_wid = self.stretchx, stretch_len = self.stretchy)
        self.paddle.penup()
        self.paddle.goto(self.xcoord, self.ycoord)

    def paddle_up(self, speed = 20):
        y = self.paddle.ycor()
        y += speed
        self.paddle.sety(y)

    def paddle_down(self, speed = 20):
        y = self.paddle.ycor()
        y -= speed
        self.paddle.sety(y)

# Paddles
paddle_a = Paddle("square", "white", -(int(disp_width / 2) - 50), 0)
paddle_a()
paddle_b = Paddle("square", "white", (int(disp_width / 2) - 50),  0)
paddle_b()

# Ball

ball          = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font=("Courier", 24, "normal"))

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a.paddle_up, "w")
wn.onkeypress(paddle_a.paddle_down, "s")

wn.onkeypress(paddle_b.paddle_up, "i")
wn.onkeypress(paddle_b.paddle_down, "k")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    if ball.ycor() > int(disp_height / 2) - 10:
        ball.sety(int(disp_height / 2) - 10)
        ball.dy *= -1
        os.system("afplay pong.mp3&")


    if ball.ycor() < -(int(disp_height / 2) - 10):
        ball.sety(-(int(disp_height / 2) - 10))
        ball.dy *= -1
        os.system("afplay pong.mp3&")



    if ball.xcor() > int(disp_width / 2) - 10:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), \
                  align = "center", font=("Courier", 24, "normal"))



    if ball.xcor() < -(int(disp_width / 2) - 10):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), \
                  align = "center", font=("Courier", 24, "normal"))


        # Paddle and ball collisions
    if (ball.xcor() > int(disp_width / 2) - 60 and ball.xcor() < int(disp_width / 2) - 50) \
        and (ball.ycor() < paddle_b.paddle.ycor() + 40 and ball.ycor() > paddle_b.paddle.ycor() - 40):
        ball.setx(int(disp_width / 2) - 60)
        ball.dx *= -1
        os.system("afplay pong.mp3&")


    if (ball.xcor() < -(int(disp_width / 2) - 60) and ball.xcor() > -(int(disp_width / 2) - 50)) \
    and (ball.ycor() < paddle_a.paddle.ycor() + 40 and ball.ycor() > paddle_a.paddle.ycor() - 40):
        ball.setx(-(int(disp_width / 2) - 60))
        ball.dx *= -1
        os.system("afplay pong.mp3&")
