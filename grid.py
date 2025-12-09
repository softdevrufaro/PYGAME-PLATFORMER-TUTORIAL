import pygame as pg  
from tile import tile
from settings import colors

class Grid: 
	def __init__(self , size , tile_size,color):
		self.size = size 
		self.tile_size = tile_size 
		self.grid = self.initiate_grid()
		self.tile = tile(tile_size,[0 , 0] , color )
		self.obstacles = {}
		self.limit = (tile_size[0] * (size[0] + 1) , tile_size[1] * (size[1] + 1))
	
	def initiate_grid(self):
		grid = []
		for y in range(self.size[1]):
			temp = []
			for x in range(self.size[0]):
				temp.append(0)
			grid.append(temp)
		return grid
	
	def draw(self , screen):
		for y , row in enumerate(self.grid):
			for x , col in enumerate(row):
				square = pg.Rect(x*self.tile_size[0] , y * self.tile_size[1] , self.tile_size[0] , self.tile_size[1])
				if col == 1: 
					pg.draw.rect(screen , colors["white"] , square)
				else: 
					pg.draw.rect(screen , colors["white"] , square , 1)
		mouse_location = self.map_mouse()
		if mouse_location:
			mouse_rect = pg.Rect(mouse_location[0] * self.tile_size[0] , mouse_location[1] * self.tile_size[1] , self.tile_size[0] , self.tile_size[1])
			pg.draw.rect(screen , colors["white"] , mouse_rect)
			if pg.mouse.get_pressed()[0]:
				if (mouse_location[0] , mouse_location[1]) in self.obstacles.keys():
						pass 
				else: 
					self.obstacles[(mouse_location[0] , mouse_location[1])] = mouse_rect
					self.grid[mouse_location[1]][mouse_location[0]] = 1
	
	def map_mouse(self):
		mouse = pg.mouse
		mouse_pos = mouse.get_pos()
		if (0<mouse_pos[0] <=self.limit[0]) and (0 < mouse_pos[1] <= self.limit[1]):
			cursor = (mouse_pos[0]//self.tile_size[0] , mouse_pos[1]//self.tile_size[1])
			return cursor
		return None
	def update(self , screen):
		self.draw(screen)