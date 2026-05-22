__version__ = "1.0.0"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(f"Calculator v{__version__}")
    print("add(2, 3) =", add(2, 3))
    print("subtract(5, 2) =", subtract(5, 2))
    print("multiply(3, 4) =", multiply(3, 4))
    print("divide(10, 2) =", divide(10, 2))
