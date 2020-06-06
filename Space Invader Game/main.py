import pygame
from pygame import mixer
import random
# Initalizing Pygame

pygame.init()

#Game Variables
window_width = 800
window_height = 600
running = True
icon_file = "ufo.png"
player_image_file = "spaceship.png"
enemy_image_file = "enemy.png"
background_image_file = "spaceBackground.jpg"
title = "Space Invader"
bullet_image_file = "bullet.png"
bg_sound_file = ""
bullet_sound_file = "match2.wav"
collision_sound_file = "badswap.wav"
game_over_thresold = 440

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

#Game Over
font_game_over = pygame.font.Font("freesansbold.ttf", 64)

# Screen
screen = pygame.display.set_mode((window_width, window_height))

# Title, Icon and Background
pygame.display.set_caption(title)
    # Icon by https://www.flaticon.com/authors/eucalyp

icon = pygame.image.load(icon_file)
pygame.display.set_icon(icon)

background = pygame.image.load(background_image_file)

# Player
playerImg = pygame.image.load(player_image_file)
playerX = 370
playerY = 480
playerX_change = 0
player_speed = 3


# Enemy 
#   Single Enemy
# enemyImg = pygame.image.load(enemy_image_file)
# enemyX = random.randint(0, 800)
# enemyY = random.randint(50 , 150)
#   Multiple Enemy
enemyImg = []
enemyX = []
enemyY = []
enemy_speed = 1.5
enemyX_change = []
enemyY_change = []
number_of_enemies = 6
for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load(enemy_image_file))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(random.choice([enemy_speed, -enemy_speed]))
    enemyY_change.append(40)

#Bullet
bulletImg = pygame.image.load(bullet_image_file)
bulletX = 0
bulletY = 480

bulletX_change = 0
bulletY_change = 3
 # bullet_state = ready --> you cant see the bullet on the screen
 #                fire --> you can see the bullet
bullet_state = "ready"

# Game Functions
def bullet_fire(x, y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y - 10))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x[i], y[i]))

def is_collision(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return True if distance < 50 else False

def show_text(x, y):
    score = font.render("Score : "+ str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    text = font_game_over.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (200, 250))

# Game Loop
while running:
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Moving player Left and Right
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                playerX_change = -player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound(bullet_sound_file)
                    bullet_sound.play()
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerX_change = 0

    # Player position update and Boundary check, so that it remains in Bound
    playerX += playerX_change
    player(playerX, playerY)
    if playerX < 0:
        playerX = 0
    elif playerX > 736 :
        playerX = 736

    # Enemy Movement
    for i in range(number_of_enemies):
        # Game Over
        if enemyY[i] > game_over_thresold:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = enemy_speed
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736 :
            enemyX_change[i] = -enemy_speed
            enemyY[i] += enemyY_change[i]
    # Collision Detection
        collision = is_collision(bulletX, bulletY, enemyX[i], enemyY[i])
        if collision and bullet_state == "fire":
            collision_sound = mixer.Sound(collision_sound_file)
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX, enemyY, i)

    # Bullet Movement
    if bulletY < 0 :
        bulletX = 0
        bulletY = playerY
        bullet_state = "ready"   
    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    
    # Showing Text on Screen
    show_text(textX, textY)

    pygame.display.update()


