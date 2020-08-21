def arithmetic_arranger(problems, solution=False):
	"""Takes list of problems (strings) and arranges them vertically.
	If solution is True returns solution with problem."""
	allowed_operators = ["+", "-"]
	if len(problems) > 5:
		return "Error: Too many problems."
			
	lines = ["" for i in range(4)]
	for problem in problems:
		parts = problem.split()
		num_length = max(len(parts[0]), len(parts[2]))
		
		if not (parts[0].isdigit() and parts[2].isdigit()):
			return "Error: Numbers must only contain digits."
		if parts[1] not in allowed_operators:
			return "Error: Operator must be '+' or '-'."
		if num_length > 4:
			return "Error: Numbers cannot be more than four digits."
		
		lines[0] += parts[0].rjust(num_length + 2) 
		lines[1] += parts[1] + " " + parts[2].rjust(num_length)
		lines[2] += "-" * (num_length + 2)
		lines[3] += str(eval(problem)).rjust(num_length + 2) 
		
		if not problem == problems[-1]:
			for i in range(len(lines)):
				lines[i] += " " * 4
				
	if not solution:
		del lines[3]	
			
	arranged_problems = "\n".join(lines)
	return arranged_problems
