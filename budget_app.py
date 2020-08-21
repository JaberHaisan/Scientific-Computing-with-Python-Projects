import itertools

class Category:
	
	def __init__(self, category):
		self.category = category.title()
		self.ledger = []
	
	def __str__(self):
		lines = []
		lines.append(self.category.center(30, "*"))
		total = 0
		for transaction in self.ledger:
			amount = float(transaction["amount"])
			total += amount
			amount = str(round(amount, 2))
			if len(amount.split(".")[1]) < 2:
				amount += "0"
				
			description = transaction["description"]
			if len(description) > 23:
				description = description[:23]
				
			line = description.ljust(23) + amount.rjust(7)
			lines.append(line)
			
		total = str(total)
		if len(total.split(".")[1]) < 2:
			total += "0"
			
		lines.append("Total: %s" % total)
		return "\n".join(lines)
	
	def deposit(self, amount, description=""):
		deposit_dict = {"amount": amount, "description": description}
		self.ledger.append(deposit_dict)
	
	def check_funds(self, amount=0):
		funds = 0
		for transaction in self.ledger:
			funds += transaction["amount"]
		return amount <= funds
		
	def withdraw(self, amount, description=""):
		done = False
		if self.check_funds(amount):
			withdraw_dict = {"amount": -amount, "description": description}
			self.ledger.append(withdraw_dict)
			done = True
		return done
	
	def get_balance(self):
		funds = 0
		for transaction in self.ledger:
			funds += transaction["amount"]
		return funds
		
	def transfer(self, amount, another_category):
		done = False
		if self.check_funds(amount):
			self.withdraw(amount, "Transfer to %s" % another_category.category)
			another_category.deposit(amount, "Transfer from %s" % self.category)
			done = True
		return done

def create_spend_chart(categories):
	data = {}
	total_spent = 0
	names = []
	
	for category in categories:
		name = category.category
		names.append(name)
		for transaction in category.ledger:
			amount = transaction["amount"]
			if amount < 0:
				data[name] = data.get(name, 0) + (-amount)
				total_spent += -amount
				
	rounded_percentages = []
	for category, amount in data.items():
		percentage = (amount / total_spent) * 100
		rounded_percentages.append(int(percentage // 10 * 10) )

	chart = ["Percentage spent by category",]
	numbers = {}
	for i in range(100,-1,-10):
		n = str(i).rjust(3)
		numbers[i] = "%s| " % n
		
	for num in rounded_percentages:
		for i in range(num, -1, -10):
			numbers[i] = numbers[i] + "o  "
		for j in range(100, num, -10):
			numbers[j] = numbers[j] + "   "
		
	
	# Number of characters for each percentage in chart with one category is 8 
	# and it increases by 3 for every new category.
	char_num = 8 + (len(categories)-1) * 3
	
	for value in numbers.values():
		chart.append(value)
	chart.append(" " * 4 + "-" * (char_num - 4))
	
	for chars in itertools.zip_longest(*names, fillvalue=" "):
		line = " " * 5 + "  ".join(chars) + "  "
		chart.append(line)

	return "\n".join(chart)
