def math_operation(x, y, operation):
    if operation == "multiply":
        return x * y
    elif operation == "divide":
        if y != 0:
            return x / y
        else:
            return "Division by zero Error"

print(math_operation(5, 3, "multiply"))
print(math_operation(6, 2, "divide"))
print(math_operation(5, 0, "divide"))

square = lambda x, y: x ** y
print(square(4, 2))

def square_def(x, y):
    return x ** y
print(square_def(4, 2))

class Rect:
    def __init__(self, x):
        self.x = x
    def __call__(self,y):
        return (self.x) * y
number = Rect(x = 5)
square = number(y = 7)
print(f'Стороны x = 5, y = 7')
print(square)