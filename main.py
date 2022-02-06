import pygame
import setup
import sprite
import image
import math

pygame.init()
pygame.display.set_caption('Periodic Table')

# create display window
SCREEN_HEIGHT = 1024
SCREEN_WIDTH = 1440

# pygame config
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# position of the table
PERIODIC_TABLE_X = 40
PERIODIC_TABLE_Y = 375

# position of the key
KEY_X = (SCREEN_WIDTH - (1086)) / 2
KEY_Y = SCREEN_HEIGHT - 40

# coordinates of table
TABLE = [[1,18],
[1,2,13,14,15,16,17,18],
[1,2,13,14,15,16,17,18]]

# create key
KEY_IMG = pygame.image.load("assets/misc/Key.svg").convert_alpha()
KEY = image.Static_Image(KEY_X, KEY_Y, KEY_IMG, 1)

# create other elements
OTHER_ELEMENTS_IMG = pygame.image.load("assets/misc/Other_elements.svg").convert_alpha()
OTHER_ELEMENTS = image.Static_Image(36, 625, OTHER_ELEMENTS_IMG, 1)

# creates instances of the images
IMAGES = []
setup.instance_imgs(IMAGES)

# create element instances, positions elements
ELEMENTS = []
setup.instance_elements(PERIODIC_TABLE_X, PERIODIC_TABLE_Y, TABLE, IMAGES, ELEMENTS)

# game loop
run = True
spawn = False
mouse = False
clock = pygame.time.Clock()

while run:
	# event handler
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = True
		if event.type == pygame.MOUSEBUTTONUP:
			# if player selects an element return element value
			if my < 369 and spawn:
				active_element = sprite.Sprite(clicked)
				print(f"Element {clicked} has been selected")
			spawn = False
			
		# quit game
		if event.type == pygame.QUIT:
			run = False

	# get the positions of the mouse
	mx,my = pygame.mouse.get_pos()

	# blue background
	SCREEN.fill((34,61,92))

	# draw the static images
	KEY.draw(SCREEN)
	OTHER_ELEMENTS.draw(SCREEN)

	# loops over all elements drawing them and checking if they have been clicked
	for i in range(18):
		if ELEMENTS[i].draw(SCREEN) and not spawn:
			clicked = i + 1
			active_element = sprite.Sprite(clicked)
			spawn = True

	#creates a sprite which tracks the mouse when you hold down
	if spawn:
		active_element.draw(SCREEN, mx ,my)

	pygame.display.update()

	clock.tick(120)

pygame.quit()