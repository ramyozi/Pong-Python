import pygame
import random

#  Pygame
pygame.init()

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# écran du jeu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# la balle et la raquette
BALL_RADIUS = 10
BALL_SPEED = 5
ball = pygame.draw.circle(screen, WHITE, (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), BALL_RADIUS)
paddle_width = 100
paddle_height = 10
paddle_x = int(SCREEN_WIDTH / 2 - paddle_width / 2)
paddle_y = SCREEN_HEIGHT - 50
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# mouvement de la balle
ball_speed_x = random.choice([-1, 1]) * BALL_SPEED
ball_speed_y = -BALL_SPEED

# l'horloge
clock = pygame.time.Clock()

# boucle de jeu
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Bouger la balle
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Vérifier la collision avec les murs
    if ball.left < 0 or ball.right > SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top < 0:
        ball_speed_y = -ball_speed_y

    # Vérifier la collision avec la raquette
    if ball.bottom >= paddle.top and ball.left >= paddle.left and ball.right <= paddle.right:
        ball_speed_y = -ball_speed_y

    # Vérifier si la balle a manqué la raquette
    if ball.bottom >= SCREEN_HEIGHT:
        game_over = True

    # Bouger la raquette
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.move_ip(5, 0)

    # Effacer l'écran
    screen.fill(BLACK)

    # Dessiner la balle et la raquette
    pygame.draw.circle(screen, WHITE, (ball.x, ball.y), BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, paddle)

    # Mettre à jour l'écran
    pygame.display.update()

    # le frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
