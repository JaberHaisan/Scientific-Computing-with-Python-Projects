import copy
import random

class Hat:
	
	def __init__(self, **balls):
		self.contents = []
		for color, number in balls.items():
			while number != 0:
				self.contents.append(color)
				number -= 1
				
	def draw(self, number_of_balls):
		if number_of_balls > len(self.contents):
			return self.contents
		else:
			result = random.sample(self.contents, number_of_balls)
			for color in result:
				self.contents.remove(color)
			return result
		
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	result = 0
	for i in range(num_experiments):
		hat_obj = copy.deepcopy(hat)
		output = {}
		for color in hat_obj.draw(num_balls_drawn):
			output[color] = output.get(color, 0) + 1
		
		match = False
		for expected_color, num in expected_balls.items():
			if expected_color not in output:
				break
			if not output[expected_color] >= num:
				break
			match = True
			
		if match:
			result += 1
			
	return result / num_experiments
			
