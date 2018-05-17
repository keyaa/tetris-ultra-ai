import sys # needed to exit in case of errors
import pyautogui # needed for keyboard actions/screenshots
import time

def click_start():
	coordinates = pyautogui.locateCenterOnScreen("ultra.png") # find the ultra logo
	if not coordinates:
		print ("Error! Could not locate Ultra logo.")
		sys.exit()
	pyautogui.click(coordinates[0]+550, coordinates[1]+450) # click start button
	return coordinates[0], coordinates[1] # return logo coordinates

def get_current_piece(ultra_x, ultra_y, piece_colors):
	# playfield coordinates

	sample_color = (0, 0, 0)
	start_check = time.time() # assert that a piece is found within 30 seconds
	while sample_color not in piece_colors.keys(): # not a valid color
		sample_color = pyautogui.pixel(ultra_x+286, ultra_y+62) # resample the color square

		if time.time() - start_check > 30: # 30 seconds exceeded (should have found a new piece at this point)
			print ("Error! No new piece discovered after a complete cycle.")
			sys.exit()
	
	return piece_colors[sample_color]

def get_next_piece(ultra_x, ultra_y, piece_colors):
	sample_color = pyautogui.pixel(ultra_x+482, ultra_y+120) # sample the next piece box

	if sample_color not in piece_colors.keys():
		sample_color = pyautogui.pixel(ultra_x+475, ultra_y+115) # I piece?

	if sample_color not in piece_colors.keys():
		sample_color = pyautogui.pixel(ultra_x+475, ultra_y+120) # O piece?
		pyautogui.moveTo(ultra_x+475, ultra_y+120)

	if sample_color not in piece_colors.keys():
		print ("Error! Failed to identify next piece.")
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

	ultra_x, ultra_y = click_start() # 634, 289 (start the game)

	playfield = [[0 for x in range(10)] for y in range(18)] # initialize playfield (10 x 18 matrix, disregard top 2 rows)

	current_piece = get_current_piece(ultra_x, ultra_y, piece_colors) # we don't know what the first piece is

	game_start = time.time() # game started, goes on for 2 minutes

	while (time.time() - game_start < 120): # ultra game is not over yet (120 seconds)
		next_piece = get_next_piece(ultra_x, ultra_y, piece_colors) # next current piece is the piece in the next box
		print ("current:", current_piece, "next:", next_piece)

		pyautogui.keyDown(" ") # can't use "press", not enough time between key-down and key-up
		time.sleep(0.1)
		pyautogui.keyUp(" ")

		current_piece = next_piece # next iteration has next piece
	
	# pyautogui.press("c")
	# pyautogui.press("left")
	# pyautogui.press("right")
	# pyautogui.press("down")
	# pyautogui.press("up")

if __name__=="__main__":
	main()