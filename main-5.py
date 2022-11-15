from art import logo
def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1*n2

def divide(n1, n2):
	return n1/n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

print (logo)
num1 = float(input("What's the first number? "))

for operandum in operations:
	print(f"{operandum}")
operandum_symbol = input("\nPick an operation from the line above. ")
num2 = float(input("What's the second number? "))

calculate = operations[operandum_symbol]
result = calculate(num1, num2)
print(f"\n{num1} {operandum_symbol} {num2} = {result}\n")

new_operation = input("Would you like to use the result for a new opration? Type 'yes' or 'no'. ").lower()
	
while new_operation == 'yes':
	for operandum in operations:
		print(f"{operandum}")
	operandum_symbol = input("\nPick an operation from the line above. ")
	num3 = float(input("What's the number? "))
	
	calculate = operations[operandum_symbol]
	new_result = calculate(result, num3)
	print(f"\n{result} {operandum_symbol} {num3} = {new_result}\n")
	new_operation = input("Would you like to use the result for a new opration? Type 'yes' or 'no'. ").lower()