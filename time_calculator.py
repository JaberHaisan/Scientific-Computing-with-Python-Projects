def add_time(start, duration, weekday=False):
	start = start.split(":")
	duration = duration.split(":")
	
	hours = int(start[0]) + int(duration[0])
	minutes = int(start[1][:2]) + int(duration[1])
	
	if minutes > 60:
		hours += minutes // 60
		minutes = minutes % 60
	
	# Finding number of days.
	initial_period = start[1][-2:]
	numerator = hours
	if initial_period == "PM":
		numerator += 12
	days = numerator // 24
	
	if hours > 24:
		hours = hours % 24
		
	# Finding new period.
	quotient = hours // 12
	if quotient % 2 == 0:
		period = initial_period
	else:
		if initial_period == "PM":
			period = "AM"
		else:
			period = "PM"
	
	if hours > 12:
		hours -= 12
	if minutes < 10:
		minutes = "0" + str(minutes)
		
	new_time = "%s:%s %s" % (hours, minutes, period)
	
	# Finding weekday for new time.
	if weekday:
		weekday = weekday.title()
		weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		
		starting_index = weekdays.index(weekday)
		next_index = starting_index 
		
		if days > 7:
			next_index += days % 7
		else:
			next_index += days
		
		if next_index > (len(weekdays) - 1):
			next_index -= 7	
      
		new_time += ", %s" % (weekdays[next_index])
		
	if days == 1:
		new_time += " (next day)"
	elif days > 1:
		new_time += " (%s days later)" % days
		
	return new_time
