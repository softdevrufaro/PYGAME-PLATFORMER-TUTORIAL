import pygame as pg  

class tile: 
	def __init__(self , size , position , color):
		self.rect = pg.Rect(position[0] , position[1] , size[0] , size[1])
		self.color = color
		self.fill = False
		self.border_width = 1
	
	def draw(self , screen):
		if self.fill:
			pg.draw.rect(screen , self.color , self.rect)
		else:
			pg.draw.rect(screen , self.color , self.rect ,self.border_width )

	def move_rect(self , position):
		self.rect.x = position[0]
		self.rect.y = position[1]
