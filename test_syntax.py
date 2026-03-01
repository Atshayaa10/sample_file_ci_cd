# Test file with syntax errors

def calculate(x, y)  # Missing :
    return x + y

for in range(5):  # Missing variable 'i'
    print("test")

def greet(name):
    print("Hello, " + name  # Missing )

if __name__ == "__main__"  # Missing :
    result = calculate(5, 3)
    print(result  # Missing )
