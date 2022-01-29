import pygame
import random 
from pygame.locals import *
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((900,600))


background = pygame.image.load("background.png")


pygame.display.set_caption("Asteroidz")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


playerImg = pygame.image.load("player.png")
playerX, playerY = 415, 480
playerX_change = 0
rect = playerImg.get_rect()


asteroidImg, asteroidX, asteroidY, asteroidY_change, rect_asteroid = [], [], [], [], [] 
total_asteroids = 10

for i in range(total_asteroids):
	asteroidImg.append(pygame.image.load("asteroids.png"))
	asteroidX.append(random.randint(100, 865))
	asteroidY.append(random.randint(10,30))
	asteroidY_change.append(8)
	rect_asteroid.append(asteroidImg[i].get_rect())


def player():
	screen.blit(playerImg, rect)
	# pygame.draw.rect(screen, (255, 0, 0), rect, 1)


def asteroid(i):
	screen.blit(asteroidImg[i], rect_asteroid[i])
	# pygame.draw.rect(screen, (255, 0, 0), rect_asteroid[i], 1)


running = True
while running:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				playerX_change = -10
			if event.key == pygame.K_d:
				playerX_change = 10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				playerX_change = 0

	screen.fill((0,0,0))
	screen.blit(background, (0,0))



	playerX += playerX_change
	rect.center = playerX, playerY+30

	if playerX <= 36: playerX = 36
	elif playerX >= 864: 
		playerX = 864

	for i in range(total_asteroids):
		
		asteroidY[i] += asteroidY_change[i]
		rect_asteroid[i].center = asteroidX[i], asteroidY[i]

		if asteroidY[i] >= 970:
			asteroidY[i] = -60
			asteroidX[i] = random.randint(36, 865)

		if pygame.Rect.colliderect(rect, rect_asteroid[i]):
			asteroidY[i] = -60
			asteroidX[i] = random.randint(36, 865)

		asteroid(i)

	
	player()
	pygame.display.update()