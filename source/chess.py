#Wombat chess
#Open source project - for more information see https://github.com/quay0/chess/
#This is a development build meaning it may contain bugs - if you find any go to https://github.com/quay0/chess/issues/new/choose and select bug report

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Hiding the greetings from the pygame comminity message

import pygame
pygame.init()

from copy import deepcopy

#Coordinates of selected square to move from
mx = 0
my = 0

#Window Setup
screen = 512+128
window = pygame.display.set_mode((screen, screen))
pygame.display.set_caption("Chess")

icon = pygame.image.load("wk.ico")

pygame.display.set_icon(icon)

#Loading sounds
sound = pygame.mixer.Sound("sound.wav")
sound_1 = pygame.mixer.Sound("sound_1.wav")

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

value = 0

#Counting piece values on the board (for AI to choose option with the highest amount of points)
def count_values():
	global value
	value = 0
	global chessboard
	aa = 0
	bb = 0
	count_loop = True
	while count_loop:
		value += test_chessboard[aa][bb]
		aa += 1
		if aa > 7:
			aa = 0
			bb += 1
		if bb > 7:
			count_loop = False

#Setting colors for board
light = (255, 255, 255)
dark = (85, 136, 182)

#Setting starting poition
#Unlike on a normal chess board (where it would be 1-8), this records positions as 0-7

chessboard = [[br,bn,bb,bq,bk,bb,bn,br],
		 [bp,bp,bp,bp,bp,bp,bp,bp],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [1,1,1,1,1,1,1,1],
		 [wp,wp,wp,wp,wp,wp,wp,wp],
		 [wr,wn,wb,wq,wk,wb,wn,wr]]

#Minimax algorithm to find best move for black
def make_best_move():
	global greatest
	global legal
	global test_chessboard
	global chessboard
	global turn

	greatest = 90000000
	count_a = 7
	count_b = 7
	while count_a >= 0:
		while count_b >= 0:
			current_piece = chessboard[count_a][count_b]

			if current_piece == br:
				new_mx = 7
				new_my = 7
				mx = count_a
				my = count_b
				while new_mx >= 0:
					while new_my >= 0:
						if mx == new_mx or my == new_my:
							f_legal = True
							if my != new_my:
								if my < new_my:
									p = my + 1
									while p < new_my:
										if chessboard[mx][p] != 1:
											f_legal = False
										p += 1
									if f_legal == True:
										legal = True
								else:
									p = my - 1
									while p > new_my:
										if chessboard[mx][p] != 1:
											f_legal = False
										p -= 1
									if f_legal == True:
										legal = True
							else:
								if mx < new_mx:
									p = mx + 1
									while p < new_mx:
										if chessboard[p][my] != 1:
											f_legal = False
										p += 1
									if f_legal == True:
										legal = True
								else:
									p = mx - 1
									while p > new_mx:
										if chessboard[p][mx] != 1:
											f_legal = False
										p -= 1
									if f_legal == True:
										legal = True
							test_chessboard = deepcopy(chessboard)
							if legal == True:
								test__chessboard = deepcopy(test_chessboard)
								test__chessboard[new_mx][new_my] = current_piece
								test__chessboard[mx][my] = 0
								count_values()
							if value < greatest:
								target = chessboard[new_mx][new_my]
								if target == wk or target == wq or target == wb or target == wn or target == wr or target == wp or target == 1:
									test_chessboard[new_mx][new_my] = current_piece
									test_chessboard[mx][my] = 0
						new_my -= 1
					new_mx -= 1
					new_my = 7

			if current_piece == bb:
				new_mx = 7
				new_my = 7
				mx = count_a
				my = count_b
				while new_mx >= 0:
					while new_my >= 0:
						x = abs(new_mx - mx)
						y = abs(new_my - my)
						if x == y and x != 0:
							legal = True
						test_chessboard = deepcopy(chessboard)
						if legal == True:
							test__chessboard = deepcopy(test_chessboard)
							test__chessboard[new_mx][new_my] = current_piece
							test__chessboard[mx][my] = 0
							count_values()
							if value < greatest:
								target = chessboard[new_mx][new_my]
								if target == wk or target == wq or target == wb or target == wn or target == wr or target == wp or target == 1:
									test_chessboard[new_mx][new_my] = current_piece
									test_chessboard[mx][my] = 0
						new_my -= 1
					new_mx -= 1
					new_my = 7

			if current_piece == bn:
				new_mx = 7
				new_my = 7
				mx = count_a
				my = count_b
				while new_mx >= 0:
					while new_my >= 0:
						if mx != new_mx or my != new_my:
							if mx == new_mx - 1 and my == new_my + 2:
								legal = True
							elif mx == new_mx + 1 and my == new_my + 2:
								legal = True
							elif mx == new_mx - 2 and my == new_my + 1:
								legal = True
							elif mx == new_mx + 2 and my == new_my + 1:
								legal = True
							elif mx == new_mx - 2 and my == new_my - 1:
								legal = True
							elif mx == new_mx + 2 and my == new_my - 1:
								legal = True
							elif mx == new_mx - 1 and my == new_my - 2:
								legal = True
							elif mx == new_mx + 1 and my == new_my - 2:
								legal = True
							test_chessboard = deepcopy(chessboard)
							if legal == True:
								test__chessboard = deepcopy(test_chessboard)
								test__chessboard[new_mx][new_my] = current_piece
								test__chessboard[mx][my] = 0
								count_values()
							if value < greatest:
								target = chessboard[new_mx][new_my]
								if target == wk or target == wq or target == wb or target == wn or target == wr or target == wp or target == 1:
									test_chessboard[new_mx][new_my] = current_piece
									test_chessboard[mx][my] = 0
						new_my -= 1
					new_mx -= 1
					new_my = 7
			
			if current_piece == bq:
				new_mx = 7
				new_my = 7
				mx = count_a
				my = count_b
				while new_mx >= 0:
					while new_my >= 0:
						if mx == new_mx or my == new_my:
							f_legal = True
							if my != new_my:
								if my < new_my:
									p = my + 1
									while p < new_my:
										if chessboard[mx][p] != 1:
											f_legal = False
										p += 1
									if f_legal == True:
										legal = True
								else:
									p = my - 1
									while p > new_my:
										if chessboard[mx][p] != 1:
											f_legal = False
										p -= 1
									if f_legal == True:
										legal = True
							else:
								if mx < new_mx:
									p = mx + 1
									while p < new_mx:
										if chessboard[p][my] != 1:
											f_legal = False
										p += 1
									if f_legal == True:
										legal = True
								else:
									p = mx - 1
									while p > new_mx:
										if chessboard[p][mx] != 1:
											f_legal = False
										p -= 1
									if f_legal == True:
										legal = True
						else:
							x = abs(new_mx - mx)
							y = abs(new_my - my)
							if x == y and x != 0:
								legal = True
						test_chessboard = deepcopy(chessboard)
						if legal == True:
							test__chessboard = deepcopy(test_chessboard)
							test__chessboard[new_mx][new_my] = current_piece
							test__chessboard[mx][my] = 0
							count_values()
							if value < greatest:
								target = chessboard[new_mx][new_my]
								if target == wk or target == wq or target == wb or target == wn or target == wr or target == wp or target == 1:
									test_chessboard[new_mx][new_my] = current_piece
									test_chessboard[mx][my] = 0
						new_my -= 1
					new_mx -= 1
					new_my = 7
				
			if current_piece == bk:
				new_mx = 7
				new_my = 7
				mx = count_a
				my = count_b
				while new_mx >= 0:
					while new_my >= 0:
						if mx == new_mx or my == new_my:
							if mx == new_mx + 1 or mx == new_mx - 1:
								legal = True
							elif my == new_my + 1 or my == new_my - 1:
								legal = True
						else:
							x = abs(new_mx - mx)
							y = abs(new_my - my)
							if x == y and x != 0:
								if mx == new_mx + 1 and my == new_my + 1:
									legal = True
								elif mx == new_mx - 1 and my == new_my - 1:
									legal = True
								elif mx == new_mx + 1 and my == new_my - 1:
									legal = True
								elif mx == new_mx - 1 and my == new_my + 1:
									legal = True
						test_chessboard = deepcopy(chessboard)
						if legal == True:
							test__chessboard = deepcopy(test_chessboard)
							test__chessboard[new_mx][new_my] = current_piece
							test__chessboard[mx][my] = 0
							count_values()
							if value < greatest:
								target = chessboard[new_mx][new_my]
								if target == wk or target == wq or target == wb or target == wn or target == wr or target == wp or target == 1:
									test_chessboard[new_mx][new_my] = current_piece
									test_chessboard[mx][my] = 0
						new_my -= 1
					new_mx -= 1
					new_my = 7

			if current_piece == bp:
				new_mx = 7
				new_my = 7
				mx = count_a
				my = count_b
				while new_mx >= 0:
					while new_my >= 0:
						if mx < 7 and my < 0:
							left = chessboard[mx + 1][my - 1]
							if left != 1:
								if new_my == my - 1 and new_mx == mx + 1:
									legal =	True
						if mx < 7 and my < 7:
							right = chessboard[mx + 1][my + 1]
							if right != 1:
								if new_my == my + 1 and new_mx == mx + 1:
									legal = True
						if mx < 7:
							piece_infront = chessboard[mx + 1][my]
							if piece_infront == 1:
								if mx == new_mx - 1 and my == new_my:
									legal = True
						if mx < 6:
							piece_infront2 = chessboard[mx + 2][my]
							if piece_infront2 == 1 and piece_infront == 1:
								if mx == 1:
									if mx == new_mx - 2 and my == new_my:
										legal = True
							test_chessboard = deepcopy(chessboard)
						if legal == True:
							test__chessboard = deepcopy(test_chessboard)
							test__chessboard[new_mx][new_my] = current_piece
							test__chessboard[mx][my] = 0
							count_values()
							if value < greatest:
								target = chessboard[new_mx][new_my]
								if target == wk or target == wq or target == wb or target == wn or target == wr or target == wp or target == 1:
									test_chessboard[new_mx][new_my] = current_piece
									test_chessboard[mx][my] = 0
						new_my -= 1
					new_mx -= 1
					new_my = 7

			count_b -= 1
		count_a -= 1
		count_b = 7
	chessboard = test_chessboard
	turn ^= 1
			

game_display = pygame.display.set_mode((512+128,512+128))
boardLength = 8
game_display.fill(light)
square_size = 64

#Drawing squares
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

#Putting the images of the pieces onto the screen to show their positions to the user
def draw_pieces():
	row = 0
	column = 0
	while row < 8:
		while column < 8:
			current = chessboard[column][row]
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
	label = font.render("Goose Chess", 1, (0,0,0))
	window.blit(label, (512, 32))
	label = font.render("New", 1, (108,85,182))
	window.blit(label, (16, 8))

legal = False

if __name__ == "__main__":
	#Main loop
	loop = True

	while loop:
		pygame.time.delay(2)
		draw_board()
		draw_pieces()
		draw_turn()

		if turn == 0:
			make_best_move()

		for event in pygame.event.get():
			#closing window
			if event.type == pygame.QUIT:
				loop = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				#If mouse clicks on 'new' reset the board and whose turn it is
				cx, cy = pygame.mouse.get_pos()
				if cx < 64 and cy < 64:
					turn = 1 #1 for white, 0 for black
					selected = False
					skip = False
					legal = False
					mx = 0
					my = 0
					chessboard = [[br,bn,bb,bq,bk,bb,bn,br],
							[bp,bp,bp,bp,bp,bp,bp,bp],
							[1,1,1,1,1,1,1,1],
							[1,1,1,1,1,1,1,1],
							[1,1,1,1,1,1,1,1],
							[1,1,1,1,1,1,1,1],
							[wp,wp,wp,wp,wp,wp,wp,wp],
							[wr,wn,wb,wq,wk,wb,wn,wr]]

				#Moving pieces
				if selected == False:
					if skip == False:
						my, mx = pygame.mouse.get_pos() #mx and my are the starting square coordinates
						mx = mx/64 - 1
						my = my/64 - 1
						mx = int(mx)
						my = int(my)
						if mx > -1 and mx < 8 and my > -1 and my < 8:
							if chessboard[mx][my] != 1:
								current = chessboard[mx][my]
								selected = True
								if current != 1:
									sound_1.play()
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


					#Legal moves
					if turn == 1:

						legal = False
						
						#King
						if current == wk:
							if mx == new_mx or my == new_my:
								if mx == new_mx + 1 or mx == new_mx - 1:
									legal = True
								elif my == new_my + 1 or my == new_my - 1:
									legal = True
							else:
								x = abs(new_mx - mx)
								y = abs(new_my - my)
								if x == y and x != 0:
									if mx == new_mx + 1 and my == new_my + 1:
										legal = True
									elif mx == new_mx - 1 and my == new_my - 1:
										legal = True
									elif mx == new_mx + 1 and my == new_my - 1:
										legal = True
									elif mx == new_mx - 1 and my == new_my + 1:
										legal = True
						
						#Rook
						if current == wr:
							if mx == new_mx or my == new_my:
								f_legal = True
								if my != new_my:
									if my < new_my:
										p = my + 1
										while p < new_my:
											if chessboard[mx][p] != 1:
												f_legal = False
											p += 1
										if f_legal == True:
											legal = True
									else:
										p = my - 1
										while p > new_my:
											if chessboard[mx][p] != 1:
												f_legal = False
											p -= 1
										if f_legal == True:
											legal = True
								else:
									if mx < new_mx:
										p = mx + 1
										while p < new_mx:
											if chessboard[p][my] != 1:
												f_legal = False
											p += 1
										if f_legal == True:
											legal = True
									else:
										p = mx - 1
										while p > new_mx:
											if chessboard[p][my] != 1:
												f_legal = False
											p -= 1
										if f_legal == True:
											legal = True
						
						#Bishop
						if current == wb:
							x = abs(new_mx - mx)
							y = abs(new_my - my)
							if x == y and x != 0:
								legal = True
						
						#Queen
						if current == wq:
							if mx == new_mx or my == new_my:
								f_legal = True
								if my != new_my:
									if my < new_my:
										p = my + 1
										while p < new_my:
											if chessboard[mx][p] != 1:
												f_legal = False
											p += 1
										if f_legal == True:
											legal = True
									else:
										p = my - 1
										while p > new_my:
											if chessboard[mx][p] != 1:
												f_legal = False
											p -= 1
										if f_legal == True:
											legal = True
								else:
									if mx < new_mx:
										p = mx + 1
										while p < new_mx:
											if chessboard[p][my] != 1:
												f_legal = False
											p += 1
										if f_legal == True:
											legal = True
									else:
										p = mx - 1
										while p > new_mx:
											if chessboard[p][mx] != 1:
												f_legal = False
											p -= 1
										if f_legal == True:
											legal = True
							else:
								x = abs(new_mx - mx)
								y = abs(new_my - my)
								if x == y and x != 0:
									legal = True
						#Knight
						if current == wn:
							if mx != new_mx or my != new_my:
								if mx == new_mx - 1 and my == new_my + 2:
									legal = True
								elif mx == new_mx + 1 and my == new_my + 2:
									legal = True
								elif mx == new_mx - 2 and my == new_my + 1:
									legal = True
								elif mx == new_mx + 2 and my == new_my + 1:
									legal = True
								elif mx == new_mx - 2 and my == new_my - 1:
									legal = True
								elif mx == new_mx + 2 and my == new_my - 1:
									legal = True
								elif mx == new_mx - 1 and my == new_my - 2:
									legal = True
								elif mx == new_mx + 1 and my == new_my - 2:
									legal = True
						
						#Pawn
						if current == wp:
							if mx > 0 and my > 0:
								left = chessboard[mx - 1][my - 1]
								if left != 1:
									if new_my == my - 1 and new_mx == mx - 1:
										legal =	True
							if mx > 0 and my < 7:
								right = chessboard[mx - 1][my + 1]
								if right != 1:
									if new_my == my + 1 and new_mx == mx - 1:
										legal = True
							if mx > 0:
								piece_infront = chessboard[mx - 1][my]
								if piece_infront == 1:
									if mx == new_mx + 1 and my == new_my:
										legal = True
							if mx > 1:
								piece_infront2 = chessboard[mx - 2][my]
								if piece_infront2 == 1 and piece_infront == 1:
									if mx == 6:
										if mx == new_mx + 2 and my == new_my:
											legal = True

						#Changing array to move pieces
						if legal == True:
							if new_mx != mx or new_my != my:
								target = chessboard[new_mx][new_my]
								if target == bk or target == bq or target == bb or target == bn or target == br or target == bp or target == 1:
									chessboard[mx][my] = 1
									chessboard[new_mx][new_my] = current
									turn ^= 1
									legal = False
									if current == wp and new_mx == 0:
										chessboard[0][new_my] = wq
								sound.play()
						selected = False
		pygame.display.update()
