import pygame
from os import listdir, system
from pyautogui import size
from getpass import getuser
pygame.init()
from Button import *
from Label import *
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
username = getuser()
font = pygame.font.Font("SFPixelate.ttf", 20)
def View_Folder(folder_path, can_go_back):
	if not can_go_back:
		go_back_button_image = pygame.image.load(r"images\go_back_button_image.png")
	else:
		go_back_button_image = pygame.image.load(r"images\go_back_button_image_2.png")
	surface_x = 40
	surface_y = 40
	surface = pygame.Surface((window_width - surface_x * 2, window_height - surface_y))
	surface_width = surface.get_width()
	surface_height = surface.get_height()
	folder_content = listdir(folder_path)
	files = []
	space = 5
	y = space
	for filename in folder_content:
		filename_label = Label(space, space, surface_width - space * 4, filename, font, (255, 255, 255))
		image = pygame.Surface((surface_width - space * 2, filename_label.height + space * 2))
		hover_image = pygame.Surface((surface_width - space * 2, filename_label.height + space * 2))
		light_rect = pygame.Surface((surface_width - space * 2, filename_label.height + space * 2))
		image.fill((30, 30, 30))
		light_rect.fill((200, 200, 200))
		light_rect.set_alpha(100)
		hover_image.blit(light_rect, (0, 0))
		filename_label.draw(image)
		filename_label.draw(hover_image)
		files.append(Button(space, y, image, hover_image, surface_x, surface_y, surface_width, surface_height))
		files[-1].filename = filename
		y += image.get_height()
	go_back_button = Button(surface_x, surface_y - go_back_button_image.get_height(), go_back_button_image, go_back_button_image, 0, 0, window_width, window_height)
	if len(files) > 1:
		can_scroll = files[-1].y + files[-1].image.get_height() > surface_height
	else:
		can_scroll = False
	while True:
		window.fill((60, 60, 60))
		surface.fill((30, 30, 30))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			for file_button in files:
				file_button.update(event)
				if file_button.pressed:
					try:
						View_Folder(fr"{folder_path}\{file_button.filename}", True)
					except:
						pygame.display.iconify()
						system(f"\"{folder_path}\{file_button.filename}\"")
			if can_scroll:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.pos[0] in range(surface_x, surface_x + surface_width) and event.pos[1] in range(surface_y, surface_y + surface_height):
						if event.button == 4:
							for file_button in files:
								file_button.y += 20
						if event.button == 5:
							for file_button in files:
								file_button.y -= 20
			if can_go_back:
				go_back_button.update(event)
		if go_back_button.pressed:
			break
		if can_scroll:
			if files[0].y > space:
				difference = files[0].y - space
				for file_button in files:
					file_button.y -= difference
			if files[-1].y + files[-1].image.get_height() < surface_height - space:
				difference = (surface_height - space) - (files[-1].y + files[-1].image.get_height())
				for file_button in files:
					file_button.y += difference
		for file_button in files:
			file_button.draw(surface)
		window.blit(surface, (surface_x, surface_y))
		go_back_button.draw(window)
		pygame.display.flip()
View_Folder(fr"C:\Users\{username}", False)