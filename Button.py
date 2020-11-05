from pygame import MOUSEBUTTONDOWN, MOUSEMOTION
class Button():
	def __init__(self, x, y, not_hover_image, hover_image, start_x, start_y, start_surface_width, start_surface_height):
		self.not_hover_image = not_hover_image
		self.hover_image = hover_image
		self.image = self.not_hover_image
		self.x = x
		self.y = y
		self.start_x = start_x
		self.start_y = start_y
		self.start_surface_width = start_surface_width
		self.start_surface_height = start_surface_height
		self.pressed = False
	def update(self, event):
		if event.type == MOUSEMOTION:
			if event.pos[0] in range(self.start_x, self.start_x + self.start_surface_width + 1) and event.pos[1] in range(self.start_y, self.start_y + self.start_surface_height + 1):
				if event.pos[0] - self.start_x in range(self.x, self.x + self.image.get_width()) and event.pos[1] - self.start_y in range(self.y, self.y + self.image.get_height()):
					self.image = self.hover_image
				else:
					self.image = self.not_hover_image
			else:
				self.image = self.not_hover_image
		if event.type == MOUSEBUTTONDOWN:
			if event.pos[0] in range(self.start_x, self.start_x + self.start_surface_width + 1) and event.pos[1] in range(self.start_y, self.start_y + self.start_surface_height + 1):
				if event.button == 1:
					if event.pos[0] - self.start_x in range(self.x, self.x + self.image.get_width()) and event.pos[1] - self.start_y in range(self.y, self.y + self.image.get_height()):
						self.pressed = True
	def draw(self, window):
		self.pressed = False
		window.blit(self.image, (self.x, self.y))