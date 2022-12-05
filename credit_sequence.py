import pygame
pygame.init()

txt_file = input("Enter the name of the text file that contains the end credit script (include .txt): ")

play_credits = True
continue_program = True
continue_data = ""

# checks to see if the continue credits file exists and collect the data if it does
try:
	continue_file = open("continue_credits.txt")
	continue_data = continue_file.readline().rstrip("\n")
	continue_file.close()
	
except FileNotFoundError:
	print("The credit sequence will restart from the beginning.")

# opens the file that contains the end credits and creates a new list to hold the credits
try:
	credit_file = open(txt_file)
	credit_list = []

	# reads each line and adds it to the new list until there are no more lines to read
	while True:
		data = credit_file.readline().rstrip("\n")
		
		if not data:
			break
			
		else:
			credit_list.append(data)
			
	credit_file.close()

except FileNotFoundError:
	print("There is no file containing the end credits. Program must exit.")
	continue_program = False

if continue_program:

	if continue_data != "":

		# finds where the continue line exists in the credit list
		resume_idx = credit_list.index(continue_data)
		
		# if the continue line is not the first line, remove the first line from the list until it is
		while resume_idx > 0:
			credit_list.pop(0)
			resume_idx -= 1
			
	# creates the screen with fixed dimension size 
	screen_width = 1000
	screen_height = 600
	screen = pygame.display.set_mode((screen_width, screen_height))

	# set starting y value for where the first line of text will be placed
	height_change = screen_height
		
	font = pygame.font.SysFont(None, 60)

	while play_credits:
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:

				# stops playing the credits
				play_credits = False
				
				# takes the last line that was played and creates a continue file containing that line
				save_data = open("continue_credits.txt", "w")
				save_data.write(credit_list[i-1] + "\n")
				save_data.close()
		
		txt_list = []
		position_list = []
		line_num = 0
		
		# iterates through each line in the credits list and render it and get its size
		for line in credit_list:
			txt = font.render(line, True, (246, 190, 20))
			txt_w, txt_h = txt.get_size()
			txt_h = 43		
			
			# the starting y value for where the text should be placed is below the screen	
			if height_change + line_num * 45 > 500:
				squish_factor = txt_h
			
			# text has been squished to a max point of 0 and will no longer be seen
			elif height_change + line_num * 45 < 12:
				squish_factor = 0
			
			# finds the y value of where the text will be placed and divide it by 12
			else: 
				squish_factor = int((height_change + line_num * 45) // 12)
			
			# rescales y value of the text and append to list
			new_txt = pygame.transform.smoothscale(txt, (txt_w, squish_factor))
			txt_list.append(new_txt)
			
			# finds where the text will be centered on screen and append to list
			txt_position = new_txt.get_rect(center = (screen_width // 2, height_change + line_num * 45)) 
			position_list.append(txt_position)
		
			line_num += 1
		
		# displays text to screen if the y value is 500 and less, decreasing starting height by 1 each time
		for i in range(line_num):
			if height_change + i * 45 > 500:
				break
				
			else:
				screen.blit(txt_list[i], position_list[i])
			
		height_change -= 1
				
		pygame.display.update()
		pygame.time.delay(30)
		screen.fill((0, 0, 0))
		
		# stops scrolling through credits if the last line has reached the top of the screen
		if height_change + i * 45 == 0:
			play_credits = False	