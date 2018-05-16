import pyautogui # needed for keyboard actions/screenshots

def orient_playfield():
	ultra_x, ultra_y = pyautogui.locateCenterOnScreen("ultra.png") # find the ultra logo
	pyautogui.click(ultra_x, ultra_y) # focus the game window, based on the logo
	return ultra_x, ultra_y # return logo coordinates

def get_current_state(playfield):
	ultra_x, ultra_y = orient_playfield() # 634, 289
	# playfield coordinates
	x = ultra_x + 184 # 818
	y = ultra_y + 46 # 335

	piece_colors = {} # RGB values of tetrominos
	# empty (0, 25, 38)
	piece_colors[(210, 76, 173)] = "T"
	piece_colors[(68, 100, 233)] = "J"
	piece_colors[(255, 126, 37)] = "L"
	piece_colors[(124, 212, 36)] = "S"
	piece_colors[(250, 50, 90)] = "Z"
	piece_colors[(50, 190, 250)] = "I"
	piece_colors[(255, 234, 76)] = "O"

	sample_color = (0, 0, 0)
	while sample_color not in piece_colors.keys(): # not a valid color
		sample_color = pyautogui.pixel(x + 102, y + 16) # resample the color square
	
	# testing, TODO: modify playfield to set all non-empty squares as filled
	pyautogui.screenshot("a.png", region=(x, y, 320, 480))

	return piece_colors[sample_color], playfield

def main():
	playfield = [[0 for x in range(10)] for y in range(18)] # initialize playfield (10 x 18 matrix, disregard top 2 rows)
	current_piece = "" # we don't know what the first piece is
	if current_piece == "":
		current_piece, playfield = get_current_state(playfield)

	for i in playfield:
		print (i)
	
	# pyautogui.press("c")
	# pyautogui.press("left")
	# pyautogui.press("right")
	# pyautogui.press("down")
	# pyautogui.press("up")
	# pyautogui.press("space")

if __name__=="__main__":
	main()