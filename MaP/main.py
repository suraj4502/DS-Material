import our_math
import greetings



def main():
    greetings.greet()
    greetings.greet_with_name(input("Enter Your name  : "))
    operator = input("""Which calculation YOU want to perform :
Enter 'a' for addition. 
Enter 's' for subtraction.
Enter 'm' for multplication.
Enter 'd' for division.
Enter 'sq' to calculate square of a number. 
: """ )
    
    # print(our_math.pi)
    
    if operator == 'a':
        a = float(input("enter the first number : "))
        b = float(input("Enter a number : "))
        result = our_math.add(a,b)
        return (f"The result is {result}.")
    
    
    elif operator == 's':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.sub(a,b)
        return (f"The result is {result}.")
    
    elif operator == 'm':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.multiply(a,b)
        return (f"The result is {result}.")
    
    elif operator == 'a':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.add(a,b)
        return (f"The result is {result}.")
    
    elif operator == 'd':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.div(a,b)
        return (f"The result is {result}.")
    
    elif operator == 'sq':
        result = our_math.square(float(input("enter the number : ")))
        return (f"The result is {result}.")

    else :
        print("Enter correcr operator.")
    

  
    

print(main())
greetings.ending()
    

# print(our_math.square(4))


