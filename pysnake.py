import pygame
from time import sleep
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 480
display_height  = 272

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

block_size = 10

FPS = 15

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])
        
def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (display_width/2), (display_height/2)
    gameDisplay.blit(textSurf, textRect)
    
def game_loop():
    gameExit = False
    gameOver = False
    
    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0
    
    snakeList = []
    snakeLength = 1
    
    randAppleX = random.randrange(0, display_width - block_size, block_size)
    randAppleY = random.randrange(0, display_height - block_size, block_size)

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen('Game over, press C to play again or Q to quit', red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]    
        
        if [x for x in snakeList[:-1] if x == snakeHead]:
            gameOver = True

        snake(block_size, snakeList)
        appleThickness = 10
        pygame.display.update()
        
        if lead_x < randAppleX + appleThickness and lead_x > randAppleX - block_size: 
            if lead_y < randAppleY + appleThickness and lead_y > randAppleY - block_size:
                randAppleX = random.randrange(0, display_width - block_size, block_size)
                randAppleY = random.randrange(0, display_height - block_size, block_size)
                snakeLength += 1

        
        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()
