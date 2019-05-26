import random
from pygame import *
import pygame

clock = time.Clock()
windowSize = (1000,1000)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128,128,128)
resolution = 10

def createZeroList(row, coll):
	matrix = [[0 for x in range(coll)] for y in range(row)] 
	return matrix
	
def printList(grid):
	print()

	for i in grid:
		print(*i)

	print()

def randomizeList(grid):
	for i in range(len(grid)):
		for j in range(len(grid)):
			array[i][j] = random.randint(0,1)

def createRandomList(row, coll):
	matrix = [[random.randint(0,1) for x in range(coll)] for y in range(row)] 
	return matrix

def count(grid, x,y):
	count = 0

	for i in range(-1, 2):
		for j in range(-1 , 2):
			count += grid[x+i][y+j]

	return count - grid[x][y]
     
def countOccurences(grid):
	count = 0 

	for i in range(len(grid)):
		for j in range(len(grid)):	

			#print("TEST")

			if grid[i][j] == 1:

				#print("FOUND")

				count = count+1
	return count

def draw(screen,grid):
	screen.fill((black))

	for i in range(len(grid)):
		for j in range(len(grid)):

			if grid[i][j] == 1:
				pygame.draw.rect(screen, gray, [j*resolution,i*resolution,resolution-1,resolution-1])

def compute(grid):

	new = createZeroList(100,100)

	for i in range(len(grid)):
		for j in range(len(grid)):

			if i ==0 or i == len(grid)-1 or j == 0 or j == len(grid)-1:
				new [i][j] = grid[i][j]
			else:

				new[i][j] = grid[i][j]

				neighbors = count(grid, i,j)
				state = grid[i][j]

				if state ==0 and neighbors == 3:
					new[i][j] = 1

				elif state == 1 and (neighbors <2 or neighbors > 3):
					new[i][j] = 0

				else:
					new[i][j] = state 
	return new

def game():
	
	main_window = display.set_mode(windowSize, RESIZABLE)
	screen = display.set_mode(windowSize,)


	array = createRandomList(100,100)
	printList(array)
	controlount = count(array,1,1)

	print(count(array,1,1))

	running = True

	init()

	# main loop
	while running:

		for e in event.get():

			if e.type == QUIT:
				running = False

		draw(screen,array)	

		#array = compute(array)
	
		display.update()
		array = compute(array)
		printList(array)
		#time.wait(10)
		
game()
