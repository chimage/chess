#Wombat chess
#Open source project for more information see https://github.com/quay0/chess/
#This is a development build meaning it may contain bugs - if you find any go to https://github.com/quay0/chess/issues/new/choose and select bug report


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Hiding the greetings from the pygame comminity message

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
_wq = pygame.image.load("wq.png")
_wk = pygame.image.load("wk.png")
_wr = pygame.image.load("wr.png")
_wb = pygame.image.load("wb.png")
_wn = pygame.image.load("wn.png")
_wp = pygame.image.load("wp.png")

_bq = pygame.image.load("bq.png")
_bk = pygame.image.load("bk.png")
_br = pygame.image.load("br.png")
_bb = pygame.image.load("bb.png")
_bn = pygame.image.load("bn.png")
_bp = pygame.image.load("bp.png")

#Piece values
bp = 100
bn = 280
bb = 320
br = 520
bq = 920
bk = 60000

wp = -100
wn = -280
wb = -320
wr = -520
wq = -920
wk = -60000

#Setting colors for board
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
#Testing starting position
position = [[1,1,1,1,1,1,1,1],
		 [1,1,1,1,bn,1,1,1],
		 [1,1,1,bk,bq,1,1,1],
		 [1,1,1,bb,br,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,wb,wq,wr],
		 [1,1,1,1,1,wn,1,1],
		 [1,1,1,1,1,1,1,wk]]

game_display = pygame.display.set_mode((512+128,512+128))
boardLength = 8
game_display.fill(light)
square_size = 64

def draw_board():
	#drawing squares
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
				#Drawing pieces
				if current == bn:
					window.blit(_bn, (((64 * row) + 74), ((64 * column) + 74)))
				if current == bb:
					window.blit(_bb, (((64 * row) + 74), ((64 * column) + 74)))
				if current == bk:
					window.blit(_bk, (((64 * row) + 74), ((64 * column) + 74)))
				if current == bq:
					window.blit(_bq, (((64 * row) + 74), ((64 * column) + 74)))
				if current == br:
					window.blit(_br, (((64 * row) + 74), ((64 * column) + 74)))
				if current == bp:
					window.blit(_bp, (((64 * row) + 74), ((64 * column) + 74)))

				if current == wn:
					window.blit(_wn, (((64 * row) + 74), ((64 * column) + 74)))
				if current == wb:
					window.blit(_wb, (((64 * row) + 74), ((64 * column) + 74)))
				if current == wk:
					window.blit(_wk, (((64 * row) + 74), ((64 * column) + 74)))
				if current == wq:
					window.blit(_wq, (((64 * row) + 74), ((64 * column) + 74)))
				if current == wr:
					window.blit(_wr, (((64 * row) + 74), ((64 * column) + 74)))
				if current == wp:
					window.blit(_wp, (((64 * row) + 74), ((64 * column) + 74)))
			column += 1
		row += 1
		column = 0

font = pygame.font.SysFont("consolas", 16)
turn = 1 #1 for white, 0 for black
selected = False
skip = False

def draw_turn():
	pygame.draw.rect(window, (255, 255, 255), (0,0,512+128,64))
	if turn == 1:
		player = "White"
	else:
		player = "Black"
	#drawing text
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

		#closing window
		if event.type == pygame.QUIT:
			loop = False

		#moving pieces
		if event.type == pygame.MOUSEBUTTONDOWN:
			if selected == False:
				if skip == False:

					if turn == 1:
						start = "w"
					else:
						start = "b"

					my, mx = pygame.mouse.get_pos() #mx and my are the starting square coordinates
					mx = mx/64 - 1
					my = my/64 - 1
					mx = int(mx)
					my = int(my)
					if mx > -1 and mx < 8 and my > -1 and my < 8:
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

				#King's legal moves
				#if current == wk or bk:
				#	if mx == new_mx or my == new_my:
				#		if mx == new_mx + 1 or mx == new_mx - 1:
				#			legal = True
				#		elif my == new_my + 1 or my == new_my - 1:
				#			legal = True
				#	else:
				#		x = abs(new_mx - mx)
				#		y = abs(new_my - my)
				#		if x == y and x != 0:
				#			if mx == x + 1 or mx == x - 1:
				#				legal = True
				#			elif my == y + 1 or my == y - 1:
				#				legal = True
				#		else:
				#			legal = False
				
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
				
				#Knights legal moves
				#if current == wn or bn:
				#	if mx != new_mx or my != new_my:
				#		x = abs(new_mx - mx)
				#		y = abs(new_my - my)
				#		if x != y and x == 0:
				#			if (mx != x + 2 or mx != x - 2) or (my != y + 2 or my != y - 2):
				#				print()
				#		else:
				#			legal = False
				#	else:
				#		legal = False
						
				#Changing array to move pieces
				if new_mx != mx or new_my != my:
					if legal == True:
						position[mx][my] = 1
						position[new_mx][new_my] = current
						turn ^= 1
						legal = False
				selected = False


	pygame.display.update()
