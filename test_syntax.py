# Test file with syntax errors

def calculate(x, y):
    return x + y

for i in range(5):
    print("test")

def greet(name):
    print("Hello, " + name)

if __name__ == "__main__":
    result = calculate(5, 3)
    print(result)
    greet("World")