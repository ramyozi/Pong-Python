import turtle

import pygame
import winsound

# Initialisation de pygame et de la musique
pygame.init()
pygame.mixer.init()

audio_file = r"C:\Users\ramzi\Desktop\aaaa.mp3"

# Initialisation de la fenêtre
wn = turtle.Screen()
wn.title("Pong by ramzi")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

# Initialisation des raquettes et de la balle
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # vitesse de l'animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)  # vitesse de l'animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)  # vitesse de l'animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = 0.08

# Initialisation du score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 21, "normal"))

# Fonctions pour déplacer les raquettes
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

# Fonction pour jouer un son
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Assignation des touches pour déplacer les raquettes
wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Boucle principale du jeu
while True:
    wn.update()

    # Mouvement de la balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Gestion des collisions avec les bords supérieurs et inférieurs de la fenêtre
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(audio_file, winsound.SND_FILENAME + winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(audio_file, winsound.SND_FILENAME + winsound.SND_ASYNC)

    # Gestion des collisions avec les bords droit et gauche de la fenetre  et mise à jour des scores
    if ball.xcor() > 390:
        paddle_b.goto(350, 0)
        paddle_a.goto(-350, 0)
        ball.goto(0, 0)
        ball.dx *= (-1)
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 21, "normal"))

    if ball.xcor() < -390:
        paddle_b.goto(350, 0)
        paddle_a.goto(-350, 0)
        ball.goto(0, 0)
        ball.dx *= (-1)
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 21, "normal"))

    # Gestion des collisions avec les raquettes
    if (340 < ball.xcor() < 350) and (
            paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(audio_file, winsound.SND_FILENAME + winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (
            paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(audio_file, winsound.SND_FILENAME + winsound.SND_ASYNC)
        
turtle.mainloop()



