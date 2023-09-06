class Atm:
    def __init__(self,pin,balance):
        self.pin = pin
        self.balance = balance
        self.menu()
        
    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to change pin
        2. Press 2 to check balance
        3. Press 3 to withdraw
        4. press 4 to add money
        5. Anything else to exit
        """)
        
        if user_input == '1':
            self.change_pin()
        elif user_input == '2':
            self.check_balance()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.credit()
        else:
            exit()


    def change_pin(self):
        old_pin = int(input('Enter old pin: '))

        if old_pin == self.pin:
            new_pin = input('Enter new pin: ')
            self.pin = new_pin
            print('Pin change successful!')
            self.menu()
        else:
            print('Cannot change pin! Incorrect old pin.')
            self.menu()


    def check_balance(self):
        old_pin = int(input('Enter old pin: '))

        if old_pin == self.pin:
            print(f"YOur balance is {self.balance}")
            self.menu()
        else :
            print("CHor chor")
            self.menu()


    def withdraw(self):
        old_pin = int(input('Enter old pin: '))

        if old_pin == self.pin:
            amount_to_withdraw = int(input("Enter the amount : "))

            if amount_to_withdraw < self.balance :
                self.balance -= amount_to_withdraw
                print(f"Amount withdrawn successfully, balance is {self.balance}")
                self.menu()
            else :
                print("Paise nahi hai tere pass itne")
                self.menu()
        else :
            print("CHor chor")
            self.menu()
    
    
    def credit(self):
        old_pin = int(input('Enter old pin: '))

        if old_pin == self.pin:
            amount_to_credit = int(input("Enter the amount : "))
            self.balance += amount_to_credit
            print(f"Amount Credit successfully, balance is {self.balance}")
            self.menu()
        else :
            print("paise dalne se pehle pin toh sahi daal.")
            self.menu()
        
    
    


atm1= Atm(111,5555)