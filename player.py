import pygame as pg  
from settings import *
# creating the player class 
class player: 
	def __init__(self , position , size ):
		self.rect = pg.Rect(position[0] , position[1] , size[0] , size[1])
		self.direction = [0 , 1]
		self.collision_dictionary = {"up":False,
							   "down":False,
							   "left":False,
							   "right":False
							   }
		self.corrected_pos = [0 , 0]
		self.collisions = []
		self.pause = True 
		self.velocity = [0 , 0]
		self.jumped = False

	def draw(self , screen):
		pg.draw.rect(screen , colors["red"] , self.rect)
	
	def read_input(self , event):
		if event.type == pg.KEYDOWN:
			if event.key in input_keys["right"]:
				self.direction[0] = 1
			if event.key in input_keys["left"]:
				self.direction[0] = -1
			if event.key in input_keys["pause/resume"]:
				if self.pause: 
					self.pause = False 
				else: 
					self.pause = True
			if event.key in input_keys["jump"] and not self.jumped:
				self.velocity[1] = -5
		elif event.type == pg.KEYUP:
			if event.key in input_keys["up"] or event.key in input_keys["down"]:
				self.direction[1] = 0
			if event.key in input_keys["right"] or event.key in input_keys["left"]:
				self.direction[0] = 0
				self.velocity[0] = 0
		else:
			pass
	
	def move(self , obstacles):
		self.calculate_velocity()
		if not self.pause:
			# Implementing movement horizontally first then vertically afterwards
			# Horizontal movement
			self.rect.x += self.direction[0] * self.velocity[0]
			for key in obstacles.keys():
				rect = obstacles[key]
				if self.rect.colliderect(rect):
					if self.direction[0] > 0 : 
						self.rect.right = rect.left 
					elif self.direction[0] < 0 : 
						self.rect.left = rect.right
					else: 
						if self.rect.x < rect.x : 
							self.rect.right = rect.left 
						else: 
							self.rect.left = rect.right
			self.rect.y += self.direction[1] * self.velocity[1]
			for key in obstacles: 
				rect = obstacles[key]
				if self.rect.colliderect(rect):
					if self.direction[1] > 0 : 
						self.rect.bottom = rect.top 
					elif self.direction[1] < 0 : 
						self.rect.top = rect.bottom 
					else: 
						if self.rect.y < rect.y: 
							self.rect.bottom = rect.top
						else: 
							self.rect.top = rect.bottom
		else: 
			pass

	def update(self,screen , obstacles):
		self.move(obstacles)
		#self.get_collisions(obstacles)
		#self.update_collision_dictionary()
		#self.adjust_player_direction()
		#self.reset_collision_flags()
		self.draw(screen)
	
	def get_collisions(self , obstacles):
		self.collisions = []
		# Checking for any existing possible collisions 
		for key in obstacles.keys():
			if self.rect.colliderect(obstacles[key]):
				self.collisions.append(obstacles[key])
	
	def update_collision_dictionary(self):
		if len(self.collisions)>0 : 
			# making the loop to check for collisions 
			for rect in self.collisions: 
				# Checking for collisions horizontally
				if self.rect.x < rect.x : 
					self.collision_dictionary["right"] = True
				elif self.rect.x > rect.x: 
					self.collision_dictionary["left"] = True
				# Checking for collisions vertically
				if self.rect.y < rect.y : 
					self.collision_dictionary["down"] = True
					if self.jumped: 
						self.jumped = False
				else: 
					self.collision_dictionary["up"] = True
	
	def adjust_player_direction(self):
		# loop to look at all the collision rects so that we can fix the player position
		for rect in self.collisions:
			# Getting the overlapping rectangle from the collisions
			clipped_rect = self.rect.clip(rect)
			# Fixing the horizontal overlap first
			if self.rect.x < rect.x: 
				if self.direction[0] == 1 :
					self.rect.right = rect.left
			else: 
				if self.direction[0] < 0:
					self.rect.left = rect.right
			# Fixing the vertical overlap second
			if self.rect.y < rect.y: 
				if self.direction[1] ==1 : 
					self.rect.bottom = rect.top
			else: 
				if self.direction[1] < 0 : 
					self.rect.top = rect.bottom
	
	def reset_collision_flags(self):
		for key in self.collision_dictionary.keys():
			self.collision_dictionary[key] = False
	
	def calculate_velocity(self):
		if self.direction[1] != 0:
				if self.velocity[1] < player_speed and self.direction[1] == 1:
					self.velocity[1] += gravity
		if self.direction[0] != 0 : 
			if self.velocity[0] < player_speed:
				self.velocity[0] += acceleration