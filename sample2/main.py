import greetings
import  my_math as m


def main():
    greetings.greet()
    o = greetings.menu()

    if o == '1':
        m.add()
    elif o == '2':
        m.sub()
    elif o =='3':
        m.mul()
    elif o =='4':
        try:
            m.div()
        except:
            print("please dont use zero in denominator.")
            m.div()
    elif o == '5':
        m.divisibility()
    elif o =='6':
        m.square()
    else:
        greetings.bye()
        exit()

    print()
    print()
    print()
    main()




main()



# from Animation import surrounding, character
#
#
# surrounding.load_surrounding()
# character.load_chararcter()

