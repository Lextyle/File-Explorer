from pygame.image import load as load_image
from pygame.transform import scale as scale_image
from pygame.event import get as get_events
from pygame import QUIT, quit, KEYDOWN, K_ESCAPE
from pygame.display import flip as update_display
from pygame.draw import rect as draw_rect
from Button import *
finish = False
def View_Picture(image_path, window, window_width, window_height):
	global finish
	image = load_image(image_path)
	while image.get_width() > window_width or image.get_height() > window_height:
		image = scale_image(image, (round(image.get_width() / 2), round(image.get_height() / 2)))
	while True:
		window.fill((30, 30, 30))
		for event in get_events():
			if event.type == QUIT:
				quit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					finish = True
		if finish:
			finish = False
			break
		window.blit(image, (window_width // 2 - image.get_width() // 2, window_height // 2 - image.get_height() // 2))
		update_display()