import our_math
import greet

from our_package import module1,module2

from our_package.module2 import function2_1



def main():
    greet.welcome()
    
    
    greet.greet(input("Enter your NAME : "))
    
    response = input("""
Select the following options :
1. Enter 1 to perform addition.
2. Enter 2 to perform subtraction.
3. Enter 3 to perform multiplication.
4. Enter 4 to perform division.
5. Enter 5 to perform squaring.
6. Enter 6 to perform square root.
7. Enter 7 to calculate area of a circle.
""")
    
    if response == '1':
        a = float(input("Enter the first number : "))
        b = float(input("Enter the second number : "))
        result = our_math.add(a,b)
        print(f"The result is : {result}")
        
    elif response == '2':
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        result = our_math.sub(a,b)
        print(f"The result is : {result}")
        
    elif response == '3':
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        result = our_math.multiply(a,b)
        print(f"The result is : {result}")
    
    elif response == '4':
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        result = our_math.div(a,b)
        print(f"The result is : {result}")
        
    elif response == '5':
        a = int(input("Enter a number : "))
        result = our_math.square(a)
        print(f"The result is : {result}")
        
    elif response == '6':
        a = int(input("Enter a number : "))
        result = our_math.square_root(a)
        print(f"The result is : {result}")
    
    elif response == '7':
        r = float(input("Enter the radius : "))
        result = our_math.area_of_circle(r,our_math.pi)
        print(f"THe area of circle is {result}")
    else:
        print("Enter a valid operation.")
    
    print()
    greet.end()
  
    
if __name__ == "__main__":
    main()