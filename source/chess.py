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

icon = pygame.image.load("wk.ico")

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

light = (255, 255, 255)
dark = (171, 122, 101)

#Setting starting poition
#Unlike on a normal chess board (where it would be 1-8), this records positions as 0-7

#position = [[br,bn,bb,bq,bk,bb,bn,br]
#		 [bp,bp,bp,bp,bp,bp,bp,bp],
#		 [1,1,1,1,1,1,1,1],
#		 [1,1,1,1,1,1,1,1],
#		 [1,1,1,1,1,1,1,1],
#		 [1,1,1,1,1,1,1,1],
#		 [wp,wp,wp,wp,wp,wp,wp,wp],
#		 [wr,wn,wb,wq,wk,wb,wn,wr]]

position = [[br,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,1,wq],
		 [1,1,bb,1,1,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,wb,1],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,bq,1,1,1,1],
		 [1,1,1,1,1,1,1,wr]]

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
legal = 0 #1 legal, 0 not legal
selected = False
skip = False

font = pygame.font.SysFont("consolas", 16)

def draw_turn():
	pygame.draw.rect(window, (255, 255, 255), (0,0,512+128,64))
	if turn == 1:
		player = "White"
	else:
		player = "Black"
	label = font.render(str(player), 1, (0,0,0))
	window.blit(label, (64, 32))
	label = font.render("0Chess", 1, (0,0,0))
	window.blit(label, (512, 32))

legal = False

#main
loop = True
while loop:
	pygame.time.delay(2)
	draw_board()
	draw_pieces()
	draw_turn()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			 loop = False
		#moving pieces
		if event.type == pygame.MOUSEBUTTONDOWN:
			if selected == False:
				if skip == False:
					my, mx = pygame.mouse.get_pos() #mx and my are the starting square coordinates
					mx = mx/64 - 1
					my = my/64 - 1
					mx = int(mx)
					my = int(my)
					if mx > -1 and mx < 8 and my > -1 and my > 8:
						if position[mx][my] != 1:
							current = position[mx][my]
							selected = True
					else:
						skip = True
				else:
					skip = False
			else:
				new_my, new_mx = pygame.mouse.get_pos() #mx and my are the target square coordinates
				new_mx = new_mx/64 - 1
				new_my = new_my/64 - 1
				new_mx = int(new_mx)
				new_my = int(new_my)

				if turn == 1:
					start = "w"
				else:
					start = "b"

				#rook = start + "r"
				#bishop = start + "b"
				#queen = start + "q"

				#exec("%s = %d" % (rook,2))
				#exec("%s = %d" % (bishop,2))
				#exec("%s = %d" % (queen,2))

				#Rook's legal moves
				if current == wr or br:
					if mx == new_mx or my == new_my:
						legal = True
					else:
						legal = False
								
				#Bishop's legal moves
				if current == wb or bb:
					x = abs(new_mx - mx)
					y = abs(new_my - my)
					if x == y and x != 0:
						legal = True
					else:
						legal = False

				#Queen's legal moves
				if current == wq or bq:
					if mx == new_mx or my == new_my:
						legal = True
					else:
						x = abs(new_mx - mx)
						y = abs(new_my - my)
						if x == y and x != 0:
							legal = True
						else:
							legal = False
						
				
				#Changing array to move pieces
				if new_mx != mx or new_my != my:
					if legal == True:
						position[mx][my] = 1
						position[new_mx][new_my] = current
						turn ^= 1
				selected = False


	pygame.display.update()
