import pygame as pg
colors = {
	"red":(255 , 0 , 0 ),
	"blue":(0 , 0 , 255),
	"black":(0 , 0 , 0 ),
	"white":(255 , 255 , 255),
	"green":(0 , 255 , 0),
}
input_keys = {
	"up":[pg.K_UP],
	"down":[pg.K_DOWN],
	"left":[pg.K_LEFT],
	"right":[pg.K_RIGHT],
	"jump":[pg.K_SPACE],
	"pause/resume":[pg.K_r , pg.K_p]
}
player_speed = 5
gravity = 0.25
acceleration = 0.25