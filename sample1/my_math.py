
pi = 3.14
def add():
    n1 = float(input("ENter first number : "))
    n2 = float(input("ENter second number : "))
    print(f"THe result is {n1 + n2}.")

def sub():
    n1 = float(input("ENter first number : "))
    n2 = float(input("ENter second number : "))
    print(f"THe result is {n1 - n2}.")

def mul():
    n1 = float(input("ENter first number : "))
    n2 = float(input("ENter second number : "))
    print(f"THe result is {n1 * n2}.")

def div():
    n1 = float(input("ENter first number : "))
    n2 = float(input("ENter second number : "))
    print(f"THe result is {n1 / n2}.")

def divisibility():
    n1 = float(input("ENter first number : "))
    n2 = float(input("ENter second number : "))
    if n1%n2 == 0:
        print(f"{n1} is divisble by {n2}")
    else:
        print("NOt divisibe.")

def square():
    n = float(input("Enter a number"))
    print(f"The result is {n ** 2}.")


