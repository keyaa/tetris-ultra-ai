import sys # needed to exit in case of errors
import pyautogui # needed for keyboard actions/screenshots
import time # to assert that no errors have occurred

def get_current_piece(ultra_x, ultra_y, piece_colors):
	# playfield coordinates

	sample_color = (0, 0, 0)
	start_check = time.time() # assert that a piece is found within 30 seconds
	while sample_color not in piece_colors.keys(): # not a valid color
		sample_color = pyautogui.pixel(ultra_x, ultra_y) # resample the color square

		if time.time() - start_check > 30: # 30 seconds exceeded (should have found a new piece at this point)
			print ("Error! No new piece discovered after a complete cycle.")
			sys.exit()
	
	return piece_colors[sample_color]

def main():
	piece_colors = {} # RGB values of tetrominos
	# empty (0, 25, 38)
	piece_colors[(210, 76, 173)] = "T"
	piece_colors[(68, 100, 233)] = "J"
	piece_colors[(255, 126, 37)] = "L"
	piece_colors[(124, 212, 36)] = "S"
	piece_colors[(250, 50, 90)] = "Z"
	piece_colors[(50, 190, 250)] = "I"
	piece_colors[(255, 194, 37)] = "O"

	playfield = [[0 for x in range(10)] for y in range(18)] # initialize playfield (10 x 18 matrix, disregard top 2 rows)

	input("Center mouse on upper squares. Press [Enter] when ready.")

	ultra_x, ultra_y = (pyautogui.position()) # set current piece detection position
	print ("Piece detection position set at: (", ultra_x, ", ", ultra_y, ")", sep="")

	pyautogui.click() # focus the window
	pyautogui.keyDown("enter") # start the game
	pyautogui.keyUp("enter") # can't use "press" for some reason

	current_piece = get_current_piece(ultra_x, ultra_y, piece_colors) # we don't know what the first piece is

	game_start = time.time() # game started, goes on for 2 minutes
	while (time.time() - game_start < 120): # ultra game is not over yet (120 seconds)
		print ("current:", current_piece)

		pyautogui.keyDown(" ")
		pyautogui.keyUp(" ")

		current_piece = get_current_piece(ultra_x, ultra_y, piece_colors) # we don't know what the first piece is
	
if __name__=="__main__":
	main()