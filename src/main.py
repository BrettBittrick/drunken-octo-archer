import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

mouseX, mouseY = 0 , 0

windowSurfaceObj = pygame.display.set_mode((640,480))
pygame.display.set_caption('Yay! pygame works!')

tileSurfaceObj = pygame.image.load('../dat/img/grass.png')

while True:
	windowSurfaceObj.fill(pygame.Color(0,0,0))
	windowSurfaceObj.blit(tileSurfaceObj, (mouseX,mouseY))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouseX, mouseY = event.pos

	pygame.display.update()
	fpsClock.tick(30)