# pong!
import pygame, sys
 
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (0, 255, 0)
# Coordinates p1, p2
x1 = (490)
y1 = 250
x2 = (0)
y2 = 250
# coordinates of the ball
xb = 500
yb = 300
speedball = 2
# horisontal and vertical direction of the ball
dbo = 0 # left
dbv = 0 # down
# Score of player 1 and 2
scorep1 = 0
scorep2 = 0
 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My game" + "Score player 1: " + str(scorep1) + " - Score player 2: " + str(scorep2))
 
pygame.init()
 
def ball():
	"Draw the ball"
	global xb, yb
	pygame.draw.ellipse(screen, PURPLE, (xb, yb, 10, 10))
 
def sprite1(y): # x and y are the mouse position
	"Draw Player 1"
	pygame.draw.rect(screen, RED, (x1, y, 10, 50))
 
def sprite2(y):
	"Draw Player 2"
	pygame.draw.rect(screen, PURPLE, (x2, y, 10, 50))
 
def move_ball(x,y):
	"The ball moves"
	global xb, yb, dbo, dbv, speedball
	if dbo == 0:
		xb -= speedball
	if dbv == 0:
		yb += speedball
		if yb > 490:
			dbv = 1
	if dbv:
		yb -= speedball
		if yb < speedball:
			dbv = 0
	if dbo:
		xb += speedball
	
def collision():
	global x1, y1 # the player 1 x and y (on the right)
	global x2, y2 # the player 2 x and y (on the left)
	global xb, yb # the ball x and y
	global x, y
	global dbo
	global scorep1, scorep2
	
	def restart():
		global xb, yb, scorep1, scorep2
		global x, y
		scorep2 += 10
		pygame.display.set_caption("My game" + "Score player 1: " + str(scorep1) + " - Score player 2: " + str(scorep2))
	
	if dbo:
		if xb > 480:
			if yb >= y and  yb < y + 50:
				dbo = 0		
			else:
				xb, yb = 10, 20
				pygame.display.update()
				pygame.time.delay(500)
				restart()
	else:
		if xb < 10:
			if yb >= y2 and  yb < y2 + 50:
				dbo = 1
			else:
				xb, yb = 480, 20
				pygame.display.update()
				pygame.time.delay(500)
				restart()

def move2():
	global y2
	if y2 <= 450:
		if keys[pygame.K_z]:
			y2 += 10
	if y2 > 0:
		if keys[pygame.K_a]:
			y2 -= 10
 
pygame.mouse.set_visible(True)
loop = 1
while loop:
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0
	x, y = pygame.mouse.get_pos()
	# move1()
	move2()
	move_ball(xb, yb)
	ball()
	sprite1(y)
	sprite2(y2)
	collision()
	pygame.display.update()
	screen.fill((0, 0, 0))
	clock.tick(60)
 
pygame.quit()
sys.exit()
