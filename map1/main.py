import my_math
import greetings

def calculate():
    inp = input("""

Select the following options :
1. Enter 1 to perform addition.
2. Enter 2 to perform subtraction.
3. Enter 3 to perform multiplication.
4. Enter 4 to perform division.
5. Enter 5 to perform squaring.
6. Enter 6 to perform square root.
7. Enter 7 to calculate area of a circle.
""")
    
    if inp == '1':
        num1 = float(input("ENter First number : "))
        num2 = float(input("ENter second number : "))
        ans = my_math.add(num1,num2)
        print(f"The result is {ans}.")
        
        
    elif inp == '2':
        num1 = float(input("ENter First number : "))
        num2 = float(input("ENter second number : "))
        ans = my_math.sub(num1,num2)
        print(f"The result is {ans}.")
        
    
    elif inp == '3':
        num1 = float(input("ENter First number : "))
        num2 = float(input("ENter second number : "))
        ans = my_math.mul(num1,num2)
        print(f"The result is {ans}.")
        
    
    elif inp == '4':
        num1 = float(input("ENter First number : "))
        num2 = float(input("ENter second number : "))
        ans = my_math.div(num1,num2)
        print(f"The result is {ans}.")
        
        
    elif inp == '5':
        num1 = float(input("ENter a number : "))
        ans = my_math.square(num1)
        print(f"The result is {ans}.")
        
    
    elif inp == '7':
        num1 = float(input("ENter a number : "))
        ans = my_math.area(num1)
        print(f"The result is {ans}.")
        
        
    else:
        print("INvalid input.")
        print("TRY AGAIN 🤓")
        calculate()


def main():
    name = input("Enter YOUR name : ")
    greetings.greet_w(name)
    print()
    greetings.greet() 
      
    calculate()
    
    print()
    greetings.end_greet()
    
    
        
        
    
    
    
main()
