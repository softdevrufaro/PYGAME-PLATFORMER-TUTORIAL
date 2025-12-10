# PYGAME-PLATFORMER-TUTORIAL
A 2D platformer template complete with a simple tilemap editor that will allow the player to draw a small map that the player can interact with

## Features
* Grid display.
  -The game will draw a 10x10 grid with 20x20 pixels squares on the grid.
  This was meant to make it easier to map the movements of the player and notice jitters or errors in the movement as well as implement a tilemap editor
* Simple Tilemap.
  -The template includes a simple tilemap that will place white squares on the grid that will serve as obstacles to the player. The tiles can be placed on the grid by left clicking the mouse.
* Collision Detection and position correction
  -The player has collision detection logic that will quickly fix their position on the grid so they do not overlap with the obstacles or go through them while moving around the map.
* Movement and jump logic.
  -The logic for movement is simple. Left and right keys to move left and right as well as a  SPACE to jump. The player also has gravity implemented that will accelerate them downwards till the reach a max speed.
* Input mapping
  -The template includes having all input being mapped to a dictionary in the settings where for development purposes it is possible to map multiple keys to perform multiple actions in the template.
## Installation
make sure that you have python version 3.13 or later

'''bash
1. git clone https://github.com/softdevrufaro/PYGAME-PLATFORMER-TUTORIAL.git
2. cd PYGAME-PLATFORMER-TUTORIAL.git
3. pip install pygame

## How to run
1. Run the main.py file in the main directory
2. Once the application is running you will see the red square at the top left corner of the screen and a black and white grid.
3. Use the mouse to draw obstacles and floors for the player, that is represented by the red square.
4. Press the R key on your keyboard and the player will start to fall down.
5. Press the LEFT and RIGHT arrow keys to move the player left and right.
6. Press the SPACE key to jump when the player is on the floor.
7. Press the ESCAPE key to exit the game loop
