import pygame
import random

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
orange = [255, 102, 0]
yellow = [255, 255, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
purple = [128, 0, 128]

FPS = 15
clock = pygame.time.Clock()

block_s = 30
screen_w, screen_h = 900, 600
assert screen_w % block_s == 0, 'Window width must be multiple of tile side.'
assert screen_h % block_s == 0, 'Window height must be multiple of tile side.'
screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
pygame.display.set_caption('Simple Top-Down Shooter')

font = pygame.font.SysFont(None, 24)

def playMusic(path):
    song = pygame.mixer.Sound(random.choice(path))
    song.play()

def message(msg, color, x, y):
    text = font.render(msg, True, color)
    screen.blit(text, [x, y])

def loadSprite(path, x, y):
    return pygame.transform.scale((pygame.image.load(path).convert_alpha()), (x,y))

gameover = loadSprite('images/gameover.png', screen_w, screen_h)
background = loadSprite('images/background.png', screen_w, screen_h)
menu = loadSprite('images/menu.png', screen_w, screen_h)

item = loadSprite('images/item.png', block_s, block_s)
vodka = loadSprite('images/powerup.png', block_s, block_s)
wall = loadSprite('images/wall.png', block_s, block_s)

leadup = loadSprite('images/leadup.png', block_s, block_s)
leaddown = loadSprite('images/leaddown.png', block_s, block_s)
leadright = loadSprite('images/leadright.png', block_s, block_s)
leadleft = loadSprite('images/leadleft.png', block_s, block_s)

enemyup = loadSprite('images/enemyup.png', block_s, block_s)
enemydown = loadSprite('images/enemydown.png', block_s, block_s)
enemyright = loadSprite('images/enemyright.png', block_s, block_s)
enemyleft = loadSprite('images/enemyleft.png', block_s, block_s)

bulletup = loadSprite('images/bulletup.png', block_s, block_s)
bulletdown = loadSprite('images/bulletdown.png', block_s, block_s)
bulletright = loadSprite('images/bulletright.png', block_s, block_s)
bulletleft = loadSprite('images/bulletleft.png', block_s, block_s)

def loadMap(path):
    wall_coords = []
    enemy_coords = []
    file = open(path, 'r')
    file = str(file.read())
    file = file.split('\\n')
    for row in range(len(file)):
        for column in range(len(file[row])):
            if file[row][column] == '@':
                lead_coords = [column*block_s, row*block_s]
            if file[row][column] == '#':
                wall_coords.append([column*block_s, row*block_s])
            if file[row][column] == 'e':
                enemy_coords.append([column*block_s, row*block_s])
    return [lead_coords, wall_coords, enemy_coords]

def mainLoop():
    lead_dir = leadup
    enemy_dir = enemyup
    lead_x_change = 0
    lead_y_change = 0
    lead_coords, wall_coords, enemy_coords = loadMap('map.txt')
    lead_x, lead_y = lead_coords

    bullet_coords = []
    bullet_dir = bulletup
    bulletMotion = False

    gameOver = False
    while True:
        while gameOver == True:
            screen.blit(gameover, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_y:
                        mainLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_dir = leadleft
                    lead_x_change = -block_s
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_dir = leadright
                    lead_x_change = block_s
                    lead
