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
	for row in range(8): # upright T
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[0]
		if sublist[1] + 1 < min_sublist:
			min_sublist = sublist[1] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for row in range(9): # T pointing to the right
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]-1][row] = 1
		temp[depths[row]-2][row] = 1
		temp[depths[row]-1][row+1] = 1
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

	for row in range(8): # T pointing down
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-1][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]-1][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[1]
		if sublist[0] + 1 < min_sublist:
			min_sublist = sublist[0] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for row in range(9): # T pointing to the left
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-1][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]-2][row+1] = 1
		playfields.append(temp)
	return playfields

def J_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1], sublist[2])) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for row in range(8): # horizontal J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-1][row] = 1
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[0]
		if sublist[1] + 2 < min_sublist:
			min_sublist = sublist[1] + 2
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for row in range(9): # upside-down J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]-1][row] = 1
		temp[depths[row]-2][row] = 1
		temp[depths[row]-2][row+1] = 1
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

	for row in range(8): # tilted J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-1][row] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]][row+2] = 1
		temp[depths[row]-1][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1])) # add it to the possible depths of dropping the piece

	for row in range(9): # upright J
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]-2][row+1] = 1
		playfields.append(temp)
	return playfields

def L_playfield(playfield, max_depth):
	width = 3 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1], sublist[2])) # add it to the possible depths of dropping the piece

	playfields = [] # possible resulting playfields
	for row in range(8): # horizontal L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]][row+2] = 1
		temp[depths[row]-1][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1])) # add it to the possible depths of dropping the piece

	for row in range(9): # upright L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]-1][row] = 1
		temp[depths[row]-2][row] = 1
		temp[depths[row]][row+1] = 1
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

	for row in range(8): # tilted L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]-1][row] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]-1][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[1]
		if sublist[0] + 2 < min_sublist:
			min_sublist = sublist[0] + 2
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for row in range(9): # upside-down L
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-2][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]-2][row+1] = 1
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
	for row in range(8): # horizontal S
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]-1][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[1]
		if sublist[0] + 1 < min_sublist:
			min_sublist = sublist[0] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for row in range(9): # vertical S
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-1][row] = 1
		temp[depths[row]-2][row] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]-1][row+1] = 1
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
	for row in range(8): # horizontal Z
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]-1][row] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]][row+1] = 1
		temp[depths[row]][row+2] = 1
		playfields.append(temp)

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		min_sublist = sublist[0]
		if sublist[1] + 1 < min_sublist:
			min_sublist = sublist[1] + 1
		depths.append(min_sublist) # add it to the possible depths of dropping the piece

	for row in range(9): # vertical Z
		temp = [row[:] for row in playfield] # make a copy of the current playfield
		temp[depths[row]][row] = 1
		temp[depths[row]-1][row] = 1
		temp[depths[row]-1][row+1] = 1
		temp[depths[row]-2][row+1] = 1
		playfields.append(temp)
	return playfields

def I_playfield(playfield, max_depth):
	width = 4 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1], sublist[2], sublist[3])) # add it to the possible depths of dropping the piece

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
		sublist = max_depth[i:i+(width)] # check spaces that are [width] wide
		depths.append(min(sublist[0], sublist[1])) # add it to the possible depths of dropping the piece

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