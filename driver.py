import sys # needed to exit in case of errors
import pyautogui # needed for keyboard actions/screenshots
import time # to assert that no errors have occurred

piece_colors = {} # RGB values of tetrominos
# empty (0, 25, 38)
piece_colors[(210, 76, 173)] = "T"
piece_colors[(68, 100, 233)] = "J"
piece_colors[(255, 126, 37)] = "L"
piece_colors[(124, 212, 36)] = "S"
piece_colors[(250, 50, 90)] = "Z"
piece_colors[(50, 190, 250)] = "I"
piece_colors[(255, 194, 37)] = "O"

def T_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)]
		min_sublist = 20
		for j in sublist: # "T" horizontally is a flat surface, find min of each depth as placement boundary
			if j < min_sublist:
				min_sublist = j
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for row in range(8): # horizontal T
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]][row+2] = 1
		playfields.append(temp)

	# TODO: >
	# TODO: v
	# TODO: <

def J_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)]
		min_sublist = 20
		for j in sublist: # "J" horizontally is a flat surface, find min of each depth as placement boundary
			if j < min_sublist:
				min_sublist = j
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for row in range(8): # horizontal J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-1][row] = 1
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]][row+2] = 1
		playfields.append(temp)

	# TODO: upside down J
	#        _____
	# TODO:      |   backwards gun
	#
	#          |
	# TODO:  _|   upright

def L_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)]
		min_sublist = 20
		for j in sublist: # "L" horizontally is a flat surface, find min of each depth as placement boundary
			if j < min_sublist:
				min_sublist = j
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for row in range(8): # horizontal L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]][row+2] = 1
		temp[depths[row]-1][row+2] = 1
		playfields.append(temp)

	# TODO: upright L
	#        _____
	# TODO: |
	# TODO: upside down L

def S_playfield(playfield, max_depth):
	pass
def Z_playfield(playfield, max_depth):
	pass
def I_playfield(playfield, max_depth):
	width = 4 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)]
		min_sublist = 20
		for j in sublist: # "I" horizontally is a flat surface, find min of each depth as placement boundary
			if j < min_sublist:
				min_sublist = j
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for row in range(7): # horizontal I
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]][row+2] = 1
		temp[depths[row]][row++3] = 1
		playfields.append(temp)
	for row in range(10): # vertical I
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[max_depth[row]][row] = 1
		temp[max_depth[row]-1][row] = 1
		temp[max_depth[row]-2][row] = 1
		temp[max_depth[row]-3][row] = 1
		playfields.append(temp)
	return playfields

def O_playfield(playfield, max_depth):
	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)]
		min_sublist = 20
		for j in sublist: # "O" is a flat surface, find min of each depth as placement boundary
			if j < min_sublist:
				min_sublist = j
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for row in range(9):
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row] = 1
		temp[depths[row]-1][row+1] = 1
		playfields.append(temp)
	return playfields

playfield_functions = {"T":T_playfield, "J":J_playfield, "L":L_playfield, "S":S_playfield, "Z":Z_playfield, "I":I_playfield, "O":O_playfield}

def get_possible_playfields(current_piece, playfield): # must return a list of posssible potential playfields
	# "O": 9 no-rotates
	# "S", "Z": 8 no-rotates, 9 one-rotates
	# "I": 7 no-rotates, 10 one-rotates
	# "J", "L", "T": 8 no-rotates, 9 one-rotates, 8 two-rotates, 9 z-rotates

	max_depth = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] # depth of each row
	for row in range(10): # for every row
		for column in range(20): # see how far deep a piece may be placed
			if playfield[column][row] == 0: # if it's empty space
				max_depth[row] += 1 # we can place it further down
			else: # otherwise, we get stopped
				break

	playfield_function = playfield_functions[current_piece]
	# playfield_function(playfield, max_depth)

	# get rid of this later
	for i in playfield_function(playfield, max_depth):
		print_playfield(i)

def get_current_piece(ultra_x, ultra_y): 
	sample_color = (-1, -1, -1) # we don't know what color the piece is yet
	start_check = time.time() # assert that a piece is found within 30 seconds
	while sample_color not in piece_colors.keys(): # not a valid color
		sample_color = pyautogui.pixel(ultra_x, ultra_y) # resample the color square
		if time.time() - start_check > 5: # 5 seconds exceeded (should have found a new piece at this point)
			print ("Error! No new piece discovered, mouse placement invalid.")
			sys.exit()
	return piece_colors[sample_color]

def print_playfield(playfield): # prints the current playfield nicely
	for i in range(10):
		print (i, end="_")
	print ("|")
	for column in range(20):
		for row in range(10):
			print (playfield[column][row], end=" ")
		print ("|", column)
	print()

def utility(playfield): # returns the utility score of a certain playfield
	return 1

def get_best_moves(current_piece, playfield): # generate possible resulting playfields and return best moves

	playfields = get_possible_playfields(current_piece, playfield) # given current playfield and piece, return list of potential results

def main():
	# playfield = []
	# i = 0
	# for column in range(20):
	# 	playfield.append([])
	# 	for row in range(10):
	# 		playfield[column].append(i)
	# 		i += 1
	playfield = [[0 for row in range(10)] for column in range(20)] # initialize playfield (10 x 20 matrix)
	playfield[4][4] = 1
	input("Center mouse on upper squares. Press [Enter] when ready.")
	ultra_x, ultra_y = (pyautogui.position()) # set current piece detection position
	print ("Piece detection position set at: (", ultra_x, ", ", ultra_y, ")", sep="")
	pyautogui.click() # focus the window
	pyautogui.keyDown("enter") # start the game
	pyautogui.keyUp("enter") # can't use "press" for some reason
	current_piece = get_current_piece(ultra_x, ultra_y) # we don't know what the first piece is yet
	game_start = time.time() # game started, goes on for 2 minutes
	while (time.time() - game_start < 120): # ultra game is not over yet (120 seconds)
		# piece placement decision logic
		best_moves = get_best_moves(current_piece, playfield)
		for move in best_moves: # execute best string of moves
			pyautogui.keyDown(move)
			pyautogui.keyUp(move)
		pyautogui.keyDown(" ") # drop the piece after positioning it optimally
		pyautogui.keyUp(" ")
		current_piece = get_current_piece(ultra_x, ultra_y) # get the next piece to play
	
if __name__=="__main__":
	main()