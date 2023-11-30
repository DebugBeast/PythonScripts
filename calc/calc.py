def add(a, b):
    answer = a + b
    print(str(a) + " + " + str( b) + " = " + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b ) + " = " + str(answer) + "\n")
def mul(a, b):
    answer = a*b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
