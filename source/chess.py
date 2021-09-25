import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

mx = 0
my = 0

#Window Setup
screen = 512+128
window = pygame.display.set_mode((screen, screen))
pygame.display.set_caption("Chess")

icon = pygame.image.load("wk.png")

pygame.display.set_icon(icon)

#Loading images
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
dark = (171, 122, 101)

#Setting starting poition
position = [[br,bn,bb,bq,bk,bb,bn,br],
		 [bp,bp,bp,bp,bp,bp,bp,bp],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [wp,wp,wp,wp,wp,wp,wp,wp],
		 [wr,wn,wb,wq,wk,wb,wn,wr]]

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
		while column < 8:
			current = position[column][row]
			if current != 1:
				window.blit(current, (((64 * row) + 74), ((64 * column) + 74)))
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
selected = False

#main
loop = True
while loop:
	pygame.time.delay(2)
	draw_board()
	draw_pieces()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			 loop = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			#moving pieces
			if selected == False:
				my, mx = pygame.mouse.get_pos()
				mx = mx/64 - 1
				my = my/64 - 1
				mx = int(mx)
				my = int(my)
				current = position[mx][my]
				selected = True
			else:
				new_my, new_mx = pygame.mouse.get_pos()
				new_mx = new_mx/64 - 1
				new_my = new_my/64 - 1
				new_mx = int(new_mx)
				new_my = int(new_my)
				if new_mx != mx or new_my != my:
					position[mx][my] = 1
					position[new_mx][new_my] = current
				selected = False


	pygame.display.update()
