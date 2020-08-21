class Rectangle:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	def __str__(self):
		return "Rectangle(width=%s, height=%s)" % (self.width, self.height)
		
	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height
	
	def get_area(self):
		return self.width * self.height
		
	def get_perimeter(self):
		return 2 * self.width + 2 * self.height
	
	def get_diagonal(self):
		return (self.width ** 2 + self.height ** 2) ** .5
	
	def get_picture(self):
		if self.width < 50 and self.height < 50:
			lines = ["*" * self.width for i in range(self.height)]
			return "\n".join(lines) + "\n"
		else:
			return "Too big for picture."
		
	def get_amount_inside(self, another_shape):
		return self.get_area() // another_shape.get_area()
		
class Square(Rectangle):
	
	def __init__(self, side):
		super().__init__(side, side)
		
	def __str__(self):
		return "Square(side=%s)" % (self.width)
    
	def set_side(self, side):
		self.width = side	
		self.height = side

	def set_width(self, width):
		self.width = width	
		self.height = width
		
	def set_height(self, height):
		self.width = height	
		self.height = height
