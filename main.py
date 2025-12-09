import pygame as pg  
from settings import * 
from player import player
from pygame.time import Clock
from grid import Grid
# Initializing pygame 
pg.init()
# Creating the screen for the pygame application 
screen = pg.display.set_mode((0 , 0) , pg.FULLSCREEN)
# Creating the player object 
Player = player([0 , 0 ] , (20 , 20))
# Importing the grid object 
grid = Grid((10 , 10) , (20 , 20) , colors['white'])
# declaring the clock 
clock = Clock()
# the main loop 
running = True 
while running : 
	screen.fill(colors["black"])
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				running = False
		if event.type == pg.QUIT:
			running = False
		Player.read_input(event)
	grid.update(screen)
	Player.update(screen , grid.obstacles)
	pg.display.flip()
	clock.tick(60)
pg.quit()