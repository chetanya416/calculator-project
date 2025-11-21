def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Example usage
print("Addition:", add(10, 20))
print("Subtraction:", subtract(20, 5))
print("Multiplication:", multiply(5, 6))
print("Division:", divide(10, 2))
