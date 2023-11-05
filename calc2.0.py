# PEACHES WAGITHI NJENGA 
# SCT211-0004/2022

class Calculator:
	def __init__(self, num1, num2, operator) -> None:
		self.num1 = num1
		self.num2 = num2
		self.operator = operator

	def sum(self):
		result = self.num1 + self.num2
		return result
	
	def subtract(self):
		result = self.num1 - self.num2
		print(result)
		return result
	
	def multiply(self):
		result = self.num1 * self.num2
		return result
	
	def divide(self):
		try:
			result = self.num1 / self.num2
		except ZeroDivisionError:
			result = 'Can not divide by 0'
		return result
	
		
def menu():
	to_eval = input("""
This is a simple calculator that takes in two integer values
adds(+), subtracts(-), multiplies(*) and divides(/) them
Enter equation to be evaluated
""")
	while True:
		if '+' in to_eval:
			delim = '+'
			break
		elif '-' in to_eval:
			delim = '-'
			break
		elif '*' in to_eval:
			delim = '*'
			break
		elif '/' in to_eval:
			delim = '/'
			break
		else:
			to_eval = input('Invalid input. Enter valid input ')


	num1 = to_eval.split(delim)
	num1 = num1[0]
	num1 = num1.strip()

	while True:
		try:
			num1 = int(num1)
			break
		except ValueError:
			num1 = input('Enter valid first number')

	num2 = to_eval.split(delim)[1].strip()
	while True:
		try:
			num2 = int(num2)
			break
		except ValueError:
			num2 = input('Enter valid Second number')


	value_list = [num1, num2, delim]
	return value_list

attributes = menu()
calc = Calculator(num1=attributes[0], num2=attributes[1], operator=attributes[2])

match attributes[2]:
	case '+':
		print(calc.sum())
	case '-':
		print(calc.subtract())
	case '*':
		print(calc.multiply())
	case '/':
		print(calc.divide())
