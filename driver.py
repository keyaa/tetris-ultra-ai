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
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1], sublist[2])) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for column in range(8): # upright T
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[0]
		if sublist[1] + 1 < min_sublist:
			min_sublist = sublist[1] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(9): # T pointing to the right
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]-1][column] = 1
		temp[depths[column]-2][column] = 1
		temp[depths[column]-1][column+1] = 1
		playfields.append(temp)

	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[1]
		if sublist[0] + 1 < min_sublist:
			min_sublist = sublist[0] + 1
		if sublist[2] + 1 < min_sublist:
			min_sublist = sublist[2] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(8): # T pointing down
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]-1][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]-1][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[1]
		if sublist[0] + 1 < min_sublist:
			min_sublist = sublist[0] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(9): # T pointing to the left
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]-1][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]-2][column+1] = 1
		playfields.append(temp)
	return playfields

def J_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1], sublist[2])) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for column in range(8): # horizontal J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]-1][column] = 1
		temp[depths[column]][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[0]
		if sublist[1] + 2 < min_sublist:
			min_sublist = sublist[1] + 2
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(9): # upside-down J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]-1][column] = 1
		temp[depths[column]-2][column] = 1
		temp[depths[column]-2][column+1] = 1
		playfields.append(temp)

	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[2]
		if sublist[0] + 1 < min_sublist:
			min_sublist = sublist[0] + 1
		if sublist[1] + 1 < min_sublist:
			min_sublist = sublist[1] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(8): # tilted J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]-1][column] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]][column+2] = 1
		temp[depths[column]-1][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1])) # add it to the possible depths of dropping the piece

	for column in range(9): # upright J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]-2][column+1] = 1
		playfields.append(temp)
	return playfields

def L_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1], sublist[2])) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for column in range(8): # horizontal L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]][column+2] = 1
		temp[depths[column]-1][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1])) # add it to the possible depths of dropping the piece

	for column in range(9): # upright L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]-1][column] = 1
		temp[depths[column]-2][column] = 1
		temp[depths[column]][column+1] = 1
		playfields.append(temp)

	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[0]
		if sublist[1] + 1 < min_sublist:
			min_sublist = sublist[1] + 1
		if sublist[2] + 1 < min_sublist:
			min_sublist = sublist[2] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(8): # tilted L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]-1][column] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]-1][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[1]
		if sublist[0] + 2 < min_sublist:
			min_sublist = sublist[0] + 2
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(9): # upside-down L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]-2][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]-2][column+1] = 1
		playfields.append(temp)
	return playfields

def S_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = min(sublist[0], sublist[1]) # bottom 2 squares
		if sublist[2] + 1 < min_sublist: # check upper square
			min_sublist = sublist[2] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for column in range(8): # horizontal S
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]-1][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[1]
		if sublist[0] + 1 < min_sublist:
			min_sublist = sublist[0] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(9): # vertical S
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]-1][column] = 1
		temp[depths[column]-2][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column+1] = 1
		playfields.append(temp)
	return playfields

def Z_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = min(sublist[1], sublist[2]) # bottom 2 squares
		if sublist[0] + 1 < min_sublist: # check upper square
			min_sublist = sublist[0] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for column in range(8): # horizontal Z
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]-1][column] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]][column+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[0]
		if sublist[1] + 1 < min_sublist:
			min_sublist = sublist[1] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for column in range(9): # vertical Z
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]-1][column] = 1
		temp[depths[column]-1][column+1] = 1
		temp[depths[column]-2][column+1] = 1
		playfields.append(temp)
	return playfields

def I_playfield(playfield, max_depth):
	width = 4 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1], sublist[2], sublist[3])) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for column in range(7): # horizontal I
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]][column+2] = 1
		temp[depths[column]][column+3] = 1
		playfields.append(temp)
	for column in range(10): # vertical I
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[max_depth[column]][column] = 1
		temp[max_depth[column]-1][column] = 1
		temp[max_depth[column]-2][column] = 1
		temp[max_depth[column]-3][column] = 1
		playfields.append(temp)
	return playfields

def O_playfield(playfield, max_depth):
	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1])) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for column in range(9):
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[column]][column] = 1
		temp[depths[column]][column+1] = 1
		temp[depths[column]-1][column] = 1
		temp[depths[column]-1][column+1] = 1
		playfields.append(temp)
	return playfields

playfield_functions = {"T":T_playfield, "J":J_playfield, "L":L_playfield, "S":S_playfield, "Z":Z_playfield, "I":I_playfield, "O":O_playfield}

def get_possible_playfields(current_piece, playfield): # must return a list of posssible potential playfields
	# "O": 9 no-rotates
	# "S", "Z": 8 no-rotates, 9 one-rotates
	# "I": 7 no-rotates, 10 one-rotates
	# "J", "L", "T": 8 no-rotates, 9 one-rotates, 8 two-rotates, 9 z-rotates
	max_depth = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] # depth of each row
	for column in range(10): # for every row
		for row in range(20): # see how far deep a piece may be placed
			if playfield[row][column] == " ": # if it's empty space
				max_depth[column] += 1 # we can place it further down
			else: # otherwise, we get stopped
				break
	playfield_function = playfield_functions[current_piece]
	return playfield_function(playfield, max_depth) # get all of the possible playfields, given current piece

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
	print()
	for row in range(20):
		for column in range(10):
			print (playfield[row][column], end=" ")
		print ("|", row)
	print()

# all possible movesets for each piece
moveset_T = {0:["left", "left", "left"], \
			1:["left", "left"], \
			2:["left"], \
			3:[""], \
			4:["right"], \
			5:["right", "right"], \
			6:["right", "right", "right"], \
			7:["right", "right", "right", "right"], \
			8:["up", "left", "left", "left", "left"], \
			9:["up", "left", "left", "left"], \
			10:["up", "left", "left"], \
			11:["up", "left"], \
			12:["up"], \
			13:["up", "right"], \
			14:["up", "right", "right"], \
			15:["up", "right", "right", "right"], \
			16:["up", "right", "right", "right", "right"], \
			17:["up", "up", "left", "left", "left"], \
			18:["up", "up", "left", "left"], \
			19:["up", "up", "left"], \
			20:["up", "up"], \
			21:["up", "up", "right"], \
			22:["up", "up", "right", "right"], \
			23:["up", "up", "right", "right", "right"], \
			24:["up", "up", "right", "right", "right", "right"], \
			25:["z", "left", "left", "left"], \
			26:["z", "left", "left"], \
			27:["z", "left"], \
			28:["z"], \
			29:["z", "right"], \
			30:["z", "right", "right"], \
			31:["z", "right", "right", "right"], \
			32:["z", "right", "right", "right", "right"], \
			33:["z", "right", "right", "right", "right", "right"]}
moveset_J = {0:["left", "left", "left"], \
			1:["left", "left"], \
			2:["left"], \
			3:[""], \
			4:["right"], \
			5:["right", "right"], \
			6:["right", "right", "right"], \
			7:["right", "right", "right", "right"], \
			8:["up", "left", "left", "left", "left"], \
			9:["up", "left", "left", "left"], \
			10:["up", "left", "left"], \
			11:["up", "left"], \
			12:["up"], \
			13:["up", "right"], \
			14:["up", "right", "right"], \
			15:["up", "right", "right", "right"], \
			16:["up", "right", "right", "right", "right"], \
			17:["up", "up", "left", "left", "left"], \
			18:["up", "up", "left", "left"], \
			19:["up", "up", "left"], \
			20:["up", "up"], \
			21:["up", "up", "right"], \
			22:["up", "up", "right", "right"], \
			23:["up", "up", "right", "right", "right"], \
			24:["up", "up", "right", "right", "right", "right"], \
			25:["z", "left", "left", "left"], \
			26:["z", "left", "left"], \
			27:["z", "left"], \
			28:["z"], \
			29:["z", "right"], \
			30:["z", "right", "right"], \
			31:["z", "right", "right", "right"], \
			32:["z", "right", "right", "right", "right"], \
			33:["z", "right", "right", "right", "right", "right"]}
moveset_L = {0:["left", "left", "left"], \
			1:["left", "left"], \
			2:["left"], \
			3:[""], \
			4:["right"], \
			5:["right", "right"], \
			6:["right", "right", "right"], \
			7:["right", "right", "right", "right"], \
			8:["up", "left", "left", "left", "left"], \
			9:["up", "left", "left", "left"], \
			10:["up", "left", "left"], \
			11:["up", "left"], \
			12:["up"], \
			13:["up", "right"], \
			14:["up", "right", "right"], \
			15:["up", "right", "right", "right"], \
			16:["up", "right", "right", "right", "right"], \
			17:["up", "up", "left", "left", "left"], \
			18:["up", "up", "left", "left"], \
			19:["up", "up", "left"], \
			20:["up", "up"], \
			21:["up", "up", "right"], \
			22:["up", "up", "right", "right"], \
			23:["up", "up", "right", "right", "right"], \
			24:["up", "up", "right", "right", "right", "right"], \
			25:["z", "left", "left", "left"], \
			26:["z", "left", "left"], \
			27:["z", "left"], \
			28:["z"], \
			29:["z", "right"], \
			30:["z", "right", "right"], \
			31:["z", "right", "right", "right"], \
			32:["z", "right", "right", "right", "right"], \
			33:["z", "right", "right", "right", "right", "right"]}
moveset_S = {0:["left", "left", "left"], \
			1:["left", "left"], \
			2:["left"], \
			3:[""], \
			4:["right"], \
			5:["right", "right"], \
			6:["right", "right", "right"], \
			7:["right", "right", "right", "right"], \
			8:["up", "left", "left", "left", "left"], \
			9:["up", "left", "left", "left"], \
			10:["up", "left", "left"], \
			11:["up", "left"], \
			12:["up"], \
			13:["up", "right"], \
			14:["up", "right", "right"], \
			15:["up", "right", "right", "right"], \
			16:["up", "right", "right", "right", "right"]}
moveset_Z = {0:["left", "left", "left"], \
			1:["left", "left"], \
			2:["left"], \
			3:[""], \
			4:["right"], \
			5:["right", "right"], \
			6:["right", "right", "right"], \
			7:["right", "right", "right", "right"], \
			8:["up", "left", "left", "left", "left"], \
			9:["up", "left", "left", "left"], \
			10:["up", "left", "left"], \
			11:["up", "left"], \
			12:["up"], \
			13:["up", "right"], \
			14:["up", "right", "right"], \
			15:["up", "right", "right", "right"], \
			16:["up", "right", "right", "right", "right"]}
moveset_I = {0:["left", "left", "left"], \
			1:["left", "left"], \
			2:["left"], \
			3:[""], \
			4:["right"], \
			5:["right", "right"], \
			6:["right", "right", "right"], \
			7:["up", "left", "left", "left", "left", "left"], \
			8:["up", "left", "left", "left", "left"], \
			9:["up", "left", "left", "left"], \
			10:["up", "left", "left"], \
			11:["up", "left"], \
			12:["up"], \
			13:["up", "right"], \
			14:["up", "right", "right"], \
			15:["up", "right", "right", "right"], \
			16:["up", "right", "right", "right", "right"]}
moveset_O = {0:["left", "left", "left", "left"], \
			1:["left", "left", "left"], \
			2:["left", "left"], \
			3:["left"], \
			4:[""], \
			5:["right"], \
			6:["right", "right"], \
			7:["right", "right", "right"], \
			8:["right", "right", "right", "right"]}
movesets = {"T":moveset_T, "J":moveset_J, "L":moveset_L, "S":moveset_S, "Z":moveset_Z, "I":moveset_I, "O":moveset_O}

def moveset_maker(current_piece, index_of_best):
	moveset_dict = movesets[current_piece]
	return moveset_dict[index_of_best]

def utility(playfield): # returns the utility score of a certain playfield
	height = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
	complete_lines = 0
	right_side_open = 1
	holes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # number of empty squares with blocks above it in a column
	# iterate through the playfield for scoring
	for row in range(20):
		line_complete = True # assume the row is complete
		for column in range(10):
			if playfield[row][column] != 1: # empty
				line_complete = False
				if height[column] != 20: # if column was sealed
					holes[column] += 1 # +1 hole count
			else: # there is a block there
				if height[column] == 20: # we can now define the height
					height[column] = row
				if column == 9: # right-hand column isn't empty
					right_side_open = 0
		if line_complete: # line cleared, shift everything up by 1
			complete_lines += 1

	height_difference = [abs(height[i+1]-height[i]) for i in range(len(height)-1)] # list of differences in heights

	if right_side_open == 0: # if the right side wasn't open
		if complete_lines == 4:
			right_side_open = 10000 # reward for making a Tetris
		else:
			right_side_open = -1000 # penalty for not keeping right side open
	else: # right side is open
		right_side_open = 200
	
	# debugging prints @@@@
	# print_playfield(playfield)
	# print ("Right side open?", right_side_open)
	# print ("complete lines:", complete_lines)
	# print ("holes:", holes)
	# print ("height", height)
	# print ("height diff", height_difference)
	# print ("final score:", 100 + (-200)*sum(holes) + (50)*complete_lines + (-100)*sum(height_difference) + right_side_open)
	# print ()

	return ((-2000)*sum(holes) + (50)*complete_lines + (-300)*sum(height_difference) + right_side_open)

def update_playfield(playfield): # remove cleared lines
	for row in range(20):
		line_complete = True # assume the row is complete
		for column in range(10):
			if playfield[row][column] != 1:
				line_complete = False
		if line_complete: # line cleared, shift everything down by 1
			# must count down (going from the bottom up)
			for row2 in range(row, 0, -1): # starting from the cleared line
				for column2 in range(10):
					playfield[row2][column2] = playfield[row2-1][column2] # everything above it comes down by 1
	for column in range(10):
		if playfield[0][column] == 1:
			print ("Pieces have reached top level, game over!")
			sys.exit()
	return playfield

def get_best_moves(current_piece, playfield): # generate possible resulting playfields and return best moves
	playfields = get_possible_playfields(current_piece, playfield) # given current playfield and piece, return list of potential results
	# call utility function on each resulting playfield, assign score, choose playfield with best score
	utilities = [] # scores assigned to each playfield
	for playfield in playfields:
		utilities.append(utility(playfield))
	# translate current piece + best playfield's index into a moveset, given index of max utility playfield
	best_utility = utilities.index(max(utilities))
	return moveset_maker(current_piece, best_utility), playfields[best_utility]

def main():
	playfield = [[" " for column in range(10)] for row in range(20)] # initialize playfield (10 x 20 matrix)
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
		best_moves, playfield = get_best_moves(current_piece, playfield)
		for move in best_moves: # execute best string of moves
			pyautogui.keyDown(move)
			pyautogui.keyUp(move)
		pyautogui.keyDown(" ") # drop the piece after positioning it optimally
		pyautogui.keyUp(" ")
		playfield = update_playfield(playfield) # clear completed lines
		current_piece = get_current_piece(ultra_x, ultra_y) # get the next piece to play
	
if __name__=="__main__":
	main()