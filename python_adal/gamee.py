import pygame
import time
import random
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 800
block_size = 20
pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

FPS = 30 

def snake(block_size, snakeList): 
  for XinY in snakeList:
    pygame.draw.rect(gameDisplay, black, [XinY[0],XinY[1],block_size,block_size])



#kóði til að birta hluti á skjáinn 
font = pygame.font.SysFont(None, 25)
def message_to_screen(msg, color):
  screen_text = font.render(msg,True,color)
  gameDisplay.blit(screen_text, [display_width/2, display_height/2])

clock = pygame.time.Clock()

def gameLoop():
  snakelist = []
  snake_length = 1
  points = 0
  gameOver = False
  gameExit = False
  lead_x = display_width/2
  lead_y = display_height/2
  lead_x_change = 0
  lead_y_change = 0

  randAppleX = round(random.randrange(0,display_width-block_size)/10.0) *10.0 
  randappleY = round(random.randrange(0,display_height-block_size)/10.0) *10.0
  pygame.display.update()
  #game loopan (snake)
  while not gameExit:
    while gameOver == True:
      gameDisplay.fill(white)
      message_to_screen('game over, press C to play again or Q to quit', red)
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            gameExit = True
            gameOver = False
          if event.key == pygame.K_c:
            gameLoop()
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
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          lead_x_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          lead_y_change = 0
    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
      gameOver = True
    AppleThickness = 30
    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,red,[randAppleX, randappleY, AppleThickness, AppleThickness])
    snakeHead = []
    snakeHead.append(lead_x)
    snakeHead.append(lead_y)
    snakelist.append(snakeHead)
    if len(snakelist) > snake_length:
      del snakelist[0]
    
    for eachSegment in snakelist[:-1]:
      if eachSegment == snakeHead:
        gameOver = True
    snake(block_size, snakelist)
    pygame.display.update()
 #   if lead_x == randAppleX and lead_y == randappleY:
 #     randAppleX = round(random.randrange(0,display_width-block_size)/10.0) *10.0 
 #     randappleY = round(random.randrange(0,display_height-block_size)/10.0) *10.0
 #     snake_length += 1
  
    if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
      if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        randAppleX = round(random.randrange(0,display_width-block_size)/10.0) *10.0 
        randappleY = round(random.randrange(0,display_height-block_size)/10.0) *10.0
        snake_length += 1
  #if lead_x > randAppleX and lead_x <randAppleX + AppleThickness or lead_x + block_size:
    clock.tick(FPS)
  pygame.quit()
  quit()
print(gameLoop())