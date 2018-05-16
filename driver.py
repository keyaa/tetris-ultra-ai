import pyautogui # needed for keyboard actions/screenshots

def orient_playfield():
	ultra_x, ultra_y = pyautogui.locateCenterOnScreen("ultra.png") # find the ultra logo
	pyautogui.click(ultra_x, ultra_y) # focus the game window, based on the logo
	return ultra_x, ultra_y # return logo coordinates

def identify_piece():
	ultra_x, ultra_y = orient_playfield()
	color_x = ultra_x + 252 # determmine coordinates for identifying the next piece
	color_y = ultra_y + 47

	# empty (0, 25, 38)
	T = (210, 76, 173)
	J = (68, 100, 233)
	L = (255, 126, 37)
	S = (124, 212, 36)
	Z = (250, 50, 90)
	I = (50, 190, 250)

	while (True): # all samples were empty (no piece at top of playfield)
		# gather samples
		sample_squares = []
		sample_squares.append(pyautogui.pixel(color_x+32, color_y+10))
		sample_squares.append(pyautogui.pixel(color_x+55, color_y+10))
		sample_squares.append(pyautogui.pixel(color_x+32, color_y+32))
		sample_squares.append(pyautogui.pixel(color_x+55, color_y+32))

		# determine what piece it is based on colors of sample squares
		if T in sample_squares:
			return "T"
		if J in sample_squares:
			return "J"
		if L in sample_squares:
			return "L"
		if S in sample_squares:
			return "S"
		if Z in sample_squares:
			return "Z"
		if I in sample_squares:
			return "I"

def main():
	current_piece = "" # we don't know what the first piece is
	if current_piece == "":
		current_piece = identify_piece()
	print (current_piece)

if __name__=="__main__":
	main()