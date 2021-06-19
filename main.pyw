# Imports
import pygame
from pygame import mixer

pygame.init()

######################################

# Templates & Functions
# Font
font = pygame.font.Font('freesansbold.ttf', 27)
# Generation function
def generate(x, y, entity):
    screen.blit(entity, (x, y))

######################################

# Audio
music = mixer.Sound('music.mp3')
music.set_volume(0.3)
music.play(-1)
ding = mixer.Sound('correct.mp3')
ding.set_volume(0.5)
crying = mixer.Sound('crying.mp3')
crying.set_volume(0.5)
slap = mixer.Sound('slap.mp3')
slap.set_volume(0.5)

######################################

# The screen
screen = pygame.display.set_mode((800, 400))

######################################

# Sprites

# Score
score = 0
textX = 10
textY = 10
scoreText = font.render("Score: " + str(score), True, (0, 0, 0))

# Lives
lives = 5
text2X = 10
text2Y = 50
liveText = font.render("Lives: " + str(lives), True, (0, 0, 0))

# Player
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg,(100, 100))
playerX = 25
playerY = 290

# Baby
babyImg = pygame.image.load('baby.png')
babyRect = babyImg.get_rect()
defaultBabyX = 95
defaultBabyY = 300
babyX = 95
babyY = 300
v = 15
m = 0.5
thrown = False

# Target
targetImg = pygame.image.load('target.png')
targetImg = pygame.transform.scale(targetImg, (75, 75))
targetRect = targetImg.get_rect()
global targetY
targetX = 725
targetY = 150
targetY_rate = 5

# Movement function
def moveTarget(n):
    global targetY
    targetY -= n

# Background
bg = pygame.image.load('bg.png')
ts = pygame.image.load('titlescreen.png')

# Caption & Icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Babies die, 2021")

######################################

# Main Game Loop
run = True
running = False
var = True
while run:
    if running == False:
        screen.blit(ts, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = True
            if event.type == pygame.QUIT:
                run = False
                break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            run = False
    while running:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and thrown == False and var == True:
                    thrown = True
        
        if targetY <= 0 or targetY >= 300:
            targetY_rate *= -1


        # throwing
        if thrown:
            F =(1 / 2)*m*(v**2)
            babyY -= F
            babyX += 25
            v = v-1
            if babyRect.colliderect(targetRect):
                ding.play()
                score += 1
                thrown = False
                babyX = defaultBabyX
                babyY = defaultBabyY
                v = 15
                m = 0.5
                if targetY_rate > 0:
                    targetY_rate += 0.3
                else:
                    targetY_rate -= 0.3
            if v<0:
                m =-0.5
            if v == -16:
                babyX = defaultBabyX
                babyY = defaultBabyY
                thrown = False
                v = 15
                m = 0.5
        if babyX >= 775:
            slap.play()
            crying.play()
            lives -= 1
            thrown = False
            babyX = defaultBabyX
            babyY = defaultBabyY
            v = 15
            m = 0.5
        if lives == 0:
            thrown = False
            var = False
            break
        
        targetRect.x = targetX
        targetRect.y = targetY
        babyRect.y = babyY
        babyRect.x = babyX
        scoreText = font.render("Score: " + str(score), True, (0, 0, 0))
        liveText = font.render("Lives: " + str(lives), True, (0, 0, 0))
        moveTarget(targetY_rate)
        generate(0, 0, bg)
        generate(playerX,playerY, playerImg)
        generate(babyX, babyY, babyImg)
        generate(targetX, targetY, targetImg)
        generate(textX, textY, scoreText)
        generate(text2X, text2Y, liveText)

        pygame.time.delay(20)
        pygame.display.update()
    pygame.display.update()