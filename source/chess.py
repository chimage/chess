import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

screen = 512

#Chess
values = {
	"Pawn": 10,
	"Knight": 30,
	"Bishop": 35,
	"Queen": 90,
	"King": 1000
}

turn = 0



loop = True
#while loop: