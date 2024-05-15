import turtle
import random

# Configuração inicial da tela
wn = turtle.Screen()
wn.title("Ping Pong com Obstáculos")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Pontuação
score_a = 0
score_b = 0

# Raquete A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Raquete B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=1, stretch_len=5)
paddle_b.penup()
paddle_b.goto(250, 0)

# Bola
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Obstáculo
obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("red")
obstacle.shapesize(stretch_wid=2, stretch_len=2)
obstacle.penup()
obstacle.goto(0, random.randint(-250, 250))

# Funções
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Controles
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Loop principal do jogo
while True:
    wn.update()

    # Mover a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Verificar colisão com a borda
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    # Verificar colisão com as raquetes
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(240)
        ball.dx *= -1
        score_b += 1

    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-240)
        ball.dx *= -1
        score_a += 1

    # Verificar colisão com o obstáculo
    if (ball.xcor() < obstacle.xcor() + 20 and ball.xcor() > obstacle.xcor() - 20) and (ball.ycor() < obstacle.ycor() + 20 and ball.ycor() > obstacle.ycor() - 20):
        ball.dx *= -1
        ball.dy *= -1

    # Atualizar a pontuação
    if score_a == 5 or score_b == 5:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        score_a = 0
        score_b = 0
        obstacle.goto(0, random.randint(-250, 250))

    # Atualizar a posição do obstáculo aleatoriamente
    if random.randint(0, 100) > 95:
        obstacle.goto(0, random.randint(-250, 250))
