import pygame
import sys
                            #written by Bryce Woodford and Binyamin Abukar


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height



pygame.init()
fps = pygame.time.Clock()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')


BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255, 236, 23)
speedx = 8
speedy = 5
speedPlayer = 0

BALL_RADIUS = 30
PAD_WIDTH = 8
PAD_HEIGHT = 140
ball = pygame.Rect(335,235,BALL_RADIUS,BALL_RADIUS)
player = pygame.Rect(680, 180, PAD_WIDTH,PAD_HEIGHT)
cpu = pygame.Rect(12, 180, PAD_WIDTH, PAD_HEIGHT)


player_speed = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 10
            if event.key == pygame.K_DOWN:
                player_speed += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 10
            if event.key == pygame.K_DOWN:
                player_speed -= 10

    if ball.top <= 0 or ball.bottom >= height:
        speedy = (speedy * -1)

    if ball.left <= 0 or ball.right >= width:
        speedx = speedx * -1

    ball.x += speedx
    ball.y += speedy
    player_animation()
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, cpu)
    pygame.draw.ellipse(screen, WHITE, ball)

    pygame.display.flip()
    fps.tick(60)