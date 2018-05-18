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

def T_playfield(playfield):
	temp = [row[:] for row in playfield] # make a copy of the current playfield
def J_playfield(playfield):
	temp = [row[:] for row in playfield] # make a copy of the current playfield
def L_playfield(playfield):
	temp = [row[:] for row in playfield] # make a copy of the current playfield
def S_playfield(playfield):
	temp = [row[:] for row in playfield] # make a copy of the current playfield
def Z_playfield(playfield):
	temp = [row[:] for row in playfield] # make a copy of the current playfield
def I_playfield(playfield):
	temp = [row[:] for row in playfield] # make a copy of the current playfield

def O_playfield(playfield): # TODO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ all of these different playfields
	temp = [row[:] for row in playfield] # make a copy of the current playfield

	max_depth = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] # depth of each row
	for row in range(10): # for every row
		for column in range(20): # see how far deep a piece may be placed
			if playfield[column][row] == 0: # if it's empty space
				max_depth[row] += 1 # we can place it further down
			else: # otherwise, we get stopped
				break

	width = 2 # width of piece
	depths = []
	for i in range(len(max_depth)-width+1): # go through the depths, creating sublists that are the piece width
		sublist = max_depth[i:i+(width)]
		depths.append(sublist) # add it to the possible depths of dropping the piece
	print (depths)

playfield_functions = {"T":T_playfield, "J":J_playfield, "L":L_playfield, "S":S_playfield, "Z":Z_playfield, "I":I_playfield, "O":O_playfield}

def get_possible_playfields(current_piece, playfield): # must return a list of posssible potential playfields
	playfield_function = playfield_functions[current_piece]

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

def utility(playfield): # returns the utility score of a certain playfield
	return 1

def get_best_moves(current_piece, playfield): # generate possible resulting playfields and return best moves
	# "O": 9 no-rotates
	# "S", "Z": 8 no-rotates, 9 one-rotates
	# "I": 7 no-rotates, 10 one-rotates
	# "J", "L", "T": 8 no-rotates, 9 one-rotates, 8 two-rotates, 9 z-rotates

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