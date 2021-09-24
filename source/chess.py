import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

screen = 512+128
window = pygame.display.set_mode((screen, screen))
pygame.display.set_caption("Chess")


wq = pygame.image.load("wq.png")
wk = pygame.image.load("wk.png")
wr = pygame.image.load("wr.png")
wb = pygame.image.load("wb.png")
wn = pygame.image.load("wn.png")
wp = pygame.image.load("wp.png")

bq = pygame.image.load("bq.png")
bk = pygame.image.load("bk.png")
br = pygame.image.load("br.png")
bb = pygame.image.load("bb.png")
bn = pygame.image.load("bn.png")
bp = pygame.image.load("bp.png")

turn = 0

light = (255, 255, 255)
dark = (42, 60, 55)


position = [[br,bn,bb,bk,bq,bb,bn,br],
		 [bp,bp,bp,bp,bp,bp,bp,bp],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [wp,wp,wp,wp,wp,wp,wp,wp],
		 [wr,wn,wb,wk,wq,wb,wn,wr]]

game_display = pygame.display.set_mode((512+128,512+128))
boardLength = 8
game_display.fill(light)
square_size = 64

def draw_board():
	count = 0
	for i in range(1,boardLength+1):
		for z in range(1,boardLength+1):
			if count % 2 == 0:
				pygame.draw.rect(game_display, light,[square_size*z,square_size*i,square_size,square_size])
			else:
				pygame.draw.rect(game_display, dark, [square_size*z,square_size*i,square_size,square_size])
			count +=1
		count-=1

def draw_pieces():
	row = 0
	column = 0
	while row < 8:
		if column < 8:
			current = [row][column]
			if current != 0:
			column += 1
		row += 1
		column = 0

values = {
	"Pawn": 10,
	"Knight": 30,
	"Bishop": 35,
	"Rook": 50,
	"Queen": 90,
	"King": 9000
}


turn = 1 #1 for white, 0 for black

#main


loop = True
while loop:
	pygame.time.delay(1000)
	draw_board()
	draw_pieces()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			 loop = False

	pygame.display.update()
