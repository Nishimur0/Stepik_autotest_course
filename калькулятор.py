def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

expression = input("Введите математическое выражение: ")

operands = []
operators = []
current_operand = ""

for char in expression:
    if char.isdigit() or char == ".":
        current_operand += char
    else:
        if current_operand:
            operands.append(float(current_operand))
            current_operand = ""
        if char in "+-/*":
            operators.append(char)

if current_operand:
    operands.append(float(current_operand))

result = operands[0]

for i in range(len(operators)):
    operator = operators[i]
    operand = operands[i + 1]

    if operator == "+":
        result = add(result, operand)
    elif operator == "-":
        result = subtract(result, operand)
    elif operator == "*":
        result = multiply(result, operand)
    elif operator == "/":
        result = divide(result, operand)

print("Результат: ", result)