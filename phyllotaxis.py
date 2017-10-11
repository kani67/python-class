#phyllotaixs.py

import pygame, math, sys, random, time


#fi = n ∗ 137.5,r = c sqrt(n)

# n is the ordering number of a floret, counting outward from the
# center. This is the reverse of floret age in a real plant

# fi  is the angle between a reference direction and the position vec-tor of the n th
#floret in a polar coordinate system originating at
#the center of the capitulum.  It follows that the
#divergence angle
#between the position vectors of any two successive florets is
#constant, angle  = 137.5◦

#r is the distance between the center of the capitulum and the 
# center of the n th floret, given a constant scaling parameter c


class Flower():

	def __init__(self):
		self.width = 800
		self.height = 600
		self.size = [self.width, self.height]
		self.number_floret = 0
		self.color = (255,0,255)
		self.constant = 8
		self.angle = 0
		self.radius = 0
		self.pos_x = 0
		self.pos_y = 0
		self.floret_angle = 137.5
		self.rect_x = 5
		self.rect_y = 5

		self.screen = pygame.display.set_mode(self.size)

		pygame.display.init()


	def draw_plant(self):
		self.angle = self.number_floret * self.floret_angle
		self.radius = self.constant * math.sqrt(self.number_floret)

		self.pos_x = self.radius * math.cos(self.angle) + self.width / 2
		self.pos_y = self.radius * math.sin(self.angle) + self.height / 2


		pygame.draw.ellipse(self.screen, self.color, [self.pos_x, self.pos_y, self.rect_x, self.rect_y])

		pygame.display.update()

		self.number_floret += 1



 

F =Flower()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit();sys.exit();

	F.draw_plant()

	time.sleep(0.01)		
	


		 	