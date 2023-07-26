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
    
    
    if operator == 's':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.sub(a,b)
        return (f"The result is {result}.")
    
    if operator == 'm':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.multiply(a,b)
        return (f"The result is {result}.")
    
    if operator == 'a':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.add(a,b)
        return (f"The result is {result}.")
    
    if operator == 'd':
        a = float(input("enter the first number : "))
        b = float(input("Enter a second number : "))
        result = our_math.div(a,b)
        return (f"The result is {result}.")
    
    if operator == 'sq':
        a = float(input("enter the number : "))
        result = our_math.square(a)
        return (f"The result is {result}.")

    
    
    

print(main())
print("Thanks for accessing this app")

# print(our_math.square(4))


