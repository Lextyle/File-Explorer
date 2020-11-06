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
python_file_icon = pygame.image.load(r"images\python_file_icon.png")
exe_file_icon = pygame.image.load(r"images\exe_file_icon.png")
image_file_icon = pygame.image.load(r"images\image_file_icon.png")
txt_file_icon = pygame.image.load(r"images\txt_file_icon.png")
folder_file_icon = pygame.image.load(r"images\folder_file_icon.png")
Pictures_icon = pygame.image.load(r"images\Pictures_icon.png")
Documents_icon = pygame.image.load(r"images\Documents_icon.png")
Downloads_icon = pygame.image.load(r"images\Downloads_icon.png")
Desktop_icon =  pygame.image.load(r"images\Desktop_icon.png")
usnecessary_folders = [fr"C:\Users\{username}\3D Objects", fr"C:\Users\{username}\Contacts", fr"C:\Users\{username}\Links", fr"C:\Users\{username}\Favorites", fr"C:\Users\{username}\.dotnet", fr"C:\Users\{username}\.designer", fr"C:\Users\{username}\.idlerc", fr"C:\Users\{username}\.android", fr"C:\Users\{username}\Videos", fr"C:\Users\{username}\Searches", fr"C:\Users\{username}\Saved Games", fr"C:\Users\{username}\OneDrive", fr"C:\Users\{username}\Music"]
Pictures_path = fr"C:\Users\{username}\Pictures"
Documents_path = fr"C:\Users\{username}\Documents"
Downloads_path = fr"C:\Users\{username}\Downloads"
Desktop_path = fr"C:\Users\{username}\Desktop"
icon_width = max(Pictures_icon.get_width(), python_file_icon.get_width(), exe_file_icon.get_width(), image_file_icon.get_width(), txt_file_icon.get_width(), folder_file_icon.get_width())
def View_Folder(folder_path, can_go_back):
	if not can_go_back:
		go_back_button_image = pygame.image.load(r"images\go_back_button_image.png")
		go_back_button_image_hover = pygame.image.load(r"images\go_back_button_image.png")
	else:
		go_back_button_image = pygame.image.load(r"images\go_back_button_image_2.png")
		go_back_button_image_hover = pygame.image.load(r"images\go_back_button_image_2_hover.png")
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
		is_folder = True
		path = fr"{folder_path}\{filename}"
		try:
			listdir(path)
		except:
			is_folder = False
		if not path in usnecessary_folders and (is_folder or filename[-3:len(filename)] == ".py" or filename[-4:len(filename)] == ".exe" or filename[-4:len(filename)] == ".png" or filename[-4:len(filename)] == ".jpg" or filename[-4:len(filename)] == ".txt"):
			filename_label = Label(space * 2 + icon_width, space, (surface_width - icon_width) - space * 5, filename, font, (255, 255, 255))
			image = pygame.Surface((surface_width - space * 2, filename_label.height + space * 2))
			hover_image = pygame.Surface((surface_width - space * 2, filename_label.height + space * 2))
			light_rect = pygame.Surface((surface_width - space * 2, filename_label.height + space * 2))
			image.fill((30, 30, 30))
			light_rect.fill((200, 200, 200))
			light_rect.set_alpha(100)
			hover_image.blit(light_rect, (0, 0))
			filename_label.draw(image)
			filename_label.draw(hover_image)
			if is_folder:
				if path == Pictures_path:
					image.blit(Pictures_icon, (space, image.get_height() // 2 - Pictures_icon.get_height() // 2))
					hover_image.blit(Pictures_icon, (space, image.get_height() // 2 - Pictures_icon.get_height() // 2))
				elif path == Documents_path:
					image.blit(Documents_icon, (space, image.get_height() // 2 - Documents_icon.get_height() // 2))
					hover_image.blit(Documents_icon, (space, image.get_height() // 2 - Documents_icon.get_height() // 2))
				elif path == Downloads_path:
					image.blit(Downloads_icon, (space, image.get_height() // 2 - Downloads_icon.get_height() // 2))
					hover_image.blit(Downloads_icon, (space, image.get_height() // 2 - Downloads_icon.get_height() // 2))
				elif path == Desktop_path:
					image.blit(Desktop_icon, (space, image.get_height() // 2 - Desktop_icon.get_height() // 2))
					hover_image.blit(Desktop_icon, (space, image.get_height() // 2 - Desktop_icon.get_height() // 2))
				else:
					image.blit(folder_file_icon, (space, image.get_height() // 2 - folder_file_icon.get_height() // 2))
					hover_image.blit(folder_file_icon, (space, image.get_height() // 2 - folder_file_icon.get_height() // 2))
			if filename[-3:len(filename)] == ".py":
				image.blit(python_file_icon, (space, image.get_height() // 2 - python_file_icon.get_height() // 2))
				hover_image.blit(python_file_icon, (space, image.get_height() // 2 - python_file_icon.get_height() // 2))
			if filename[-4:len(filename)] == ".exe":
				image.blit(exe_file_icon, (space, image.get_height() // 2 - image_file_icon.get_height() // 2))
				hover_image.blit(exe_file_icon, (space, image.get_height() // 2 - exe_file_icon.get_height() // 2))
			if filename[-4:len(filename)] == ".png" or filename[-4:len(filename)] == ".jpg":
				image.blit(image_file_icon, (space, image.get_height() // 2 - image_file_icon.get_height() // 2))
				hover_image.blit(image_file_icon, (space, image.get_height() // 2 - image_file_icon.get_height() // 2))
			if filename[-4:len(filename)] == ".txt":
				image.blit(txt_file_icon, (space, image.get_height() // 2 - txt_file_icon.get_height() // 2))
				hover_image.blit(txt_file_icon, (space, image.get_height() // 2 - txt_file_icon.get_height() // 2))
			files.append(Button(space, y, image, hover_image, surface_x, surface_y, surface_width, surface_height))
			files[-1].filename = filename
			y += image.get_height()
	go_back_button = Button(surface_x, surface_y - go_back_button_image.get_height(), go_back_button_image, go_back_button_image_hover, 0, 0, window_width, window_height)
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
		if files[0].y < 0:
			black_surface = pygame.Surface((surface_width, 20))
			black_surface.fill((0, 0, 0))
			black_surface.set_alpha(100)
			surface.blit(black_surface, (0, 0))
		window.blit(surface, (surface_x, surface_y))
		go_back_button.draw(window)
		pygame.display.flip()
View_Folder(fr"C:\Users\{username}", False)