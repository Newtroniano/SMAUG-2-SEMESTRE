import math , random , sys
import pygame
from pygame.locals import *

def events():
    for event in pygame.event.get ():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit ()
            sys.exit ()





W , H = 1080 , 720
HW , HH = W / 2 , H / 2
AREA = W * H





pygame.init ()
CLOCK = pygame.time.Clock ()
DS = pygame.display.set_mode ( (W , H) )
pygame.display.set_caption ( "code.Pylet - Scrolling Background with Player" )
FPS = 500


BLACK = (0 , 0 , 0 , 255)
WHITE = (255 , 255 , 255 , 255)

bg = pygame.image.load ( "teste.png" ).convert ()
bgWidth , bgHeight = bg.get_rect ().size

stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 585
playerVelocityX = 0
playerVelocityY = 0

# main loop
while True:


    events ()

    k = pygame.key.get_pressed ()

    if k[K_RIGHT]:
        playerVelocityX = 1
    elif k[K_LEFT]:
        playerVelocityX = -1
    else:
        playerVelocityX = 0

    playerPosX += playerVelocityX
    if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
    if playerPosX < circleRadius: playerPosX = circleRadius
    if playerPosX < startScrollingPosX:
        circlePosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX:
        circlePosX = playerPosX - stageWidth + W
    else:
        circlePosX = startScrollingPosX
        stagePosX += -playerVelocityX






    rel_x = stagePosX % bgWidth
    DS.blit ( bg , (rel_x - bgWidth , 0) )
    if rel_x < W:
        DS.blit ( bg , (rel_x , 0) )

    pygame.draw.circle ( DS , WHITE ,  (int(circlePosX),playerPosY - circleRadius), circleRadius,0)

    pygame.display.update ()
    CLOCK.tick ( FPS )
    DS.fill ( BLACK )



