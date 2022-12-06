import pygame
import sys
                            #written by Bryce Woodard and Binyamin Abukar


def player_animation():
    player.y += playerspeed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

def player2_animation():
    player2.y += player2speed

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= height:
        player2.bottom = height


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

BALL_RADIUS = 40
PAD_WIDTH = 8
PAD_HEIGHT = 140
ball = pygame.Rect(335,235,BALL_RADIUS,BALL_RADIUS)
player = pygame.Rect(680, 180, PAD_WIDTH,PAD_HEIGHT)
player2 = pygame.Rect(12, 180, PAD_WIDTH, PAD_HEIGHT)

# score 1 -> p1
# score 2 -> p2
score1 = 0
score2 = 0

playerspeed = 0
player2speed = 0

# Function to display the scores
# Written by BW
def SetText(screen, text, x, y):
    try:
        text = str(text)
        font = pygame.font.SysFont("Comic Sans MS", 20)
        text = font.render(text, True, WHITE)
        screen.blit(text, (x, y))

    except Exception as e:
        print ("Font Error")
        raise e 

# Function to reset the ball position after a win, however it keeps the speed 
def Reset():
    ball.x = 325
    ball.y = 325

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerspeed -= 10
            if event.key == pygame.K_DOWN:
                playerspeed += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerspeed += 10
            if event.key == pygame.K_DOWN:
                playerspeed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player2speed -= 10
            if event.key == pygame.K_w:
                player2speed += 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player2speed += 10
            if event.key == pygame.K_w:
                player2speed -= 10

    if ball.top <= 0 or ball.bottom >= height:
        speedy = (speedy * -1)

    if ball.left <= 0:
        score2 += 1
        Reset()
    if ball.right >= width:
        score1 += 1
        Reset()

    ball.x += speedx
    ball.y += speedy
    player_animation()
    player2_animation()

    if player.colliderect(ball):
        speedx *= -1
    if player2.colliderect(ball):
        speedx *= -1

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    SetText(screen, str(score1),  100, 50)
    SetText(screen, "SCORE", 300, 50)
    SetText(screen, str(score2), 600, 50)
    pygame.display.flip()

    fps.tick(60)
