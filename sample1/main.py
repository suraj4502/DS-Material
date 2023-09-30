import  greetings
import my_math as m


# package related
# from my_package import my_file,module2
# import my_package
#
# my_package.module2.my_func()
#
# my_file.my_func()

def main():
    greetings.greet()
    o= greetings.menu()

    if o == '1':
        m.add()

    elif o == '2':
        m.sub()

    elif o == '3':
        m.mul()

    elif o == '4':
        m.div()

    elif o == '5':
        m.divisibility()

    elif o == '6':
        m.square()

    else:
        greetings.bye()
        exit()

    print()
    print()
    print()
    main()




main()
