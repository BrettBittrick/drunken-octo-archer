import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

#sets the window size
windowX, windowY = 1024 , 768

#sets the map size (in tiles)
mapX, mapY = 256, 256

#size of the tiles
tileSize = 16

#the number of tiles that can be rendered in the window
tilesX = (windowX / tileSize) + 1 # add .5 so we'll render a tile even if it's only partially on the map
tilesY = (windowY / tileSize) + 1

mouseX, mouseY = 0 , 0

windowSurfaceObj = pygame.display.set_mode((windowX,windowY))
pygame.display.set_caption('It begins')

tileSurfaceObj = pygame.image.load('../dat/img/grass.png')
selectSurfaceObj = pygame.image.load('../dat/img/select.png')

class Tile(object):
	"""Base tile"""
	def __init__(self, art):
		self.art = art
	def GetArt(self):
		return self.art
		
t = Tile(tileSurfaceObj)

while True:
	windowSurfaceObj.fill(pygame.Color(0,0,0))
	
	for tileY in range(tilesY):
		for tileX in range(tilesX):
			windowSurfaceObj.blit(t.GetArt(), (tileX * tileSize, tileY * tileSize))
			
	#this is probably pretty slow, I'll revise this later
	windowSurfaceObj.blit(selectSurfaceObj, ( mouseX - (mouseX % tileSize),mouseY - (mouseY % tileSize)))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouseX, mouseY = event.pos

	pygame.display.update()
	fpsClock.tick(30)