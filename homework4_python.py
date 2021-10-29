import unittest

class Atm_simulator:
    def atm_entry(self):
        '''

        '''
        # defining the variables
        self.pin='1234'
        self.pin_input = input('Please put your pin: ')
        self.account_balance = 100
        count = 0
        pin_count = 3

        while count < 3:
            if self.pin_input == self.pin:
                break

            elif self.pin_input != self.pin:
                pin_input=input('incorrect pin: you have {} more tries: '.format(pin_count))
                count+=1
                pin_count-=1

        if count > 2:
            print('Invalid pin 3 times. Exiting the program')
            exit()

        y = print('Correct pin')
        return y 


    def cash_withdrawal(self):
        '''

        '''
        is_Successful = False
        try:
            self.withdrawal_amount = int(input('Please input a withdrawal amount: '))
        except Exception as e:
            print("Value entered is not a valid number")
            print(str(e))

        try:
            if self.account_balance > withdrawal_amount:
                self.remaining_balance = self.account_balance - withdrawal_amount
                print('Your remaining balance is: {}'.format(remaining_balance))
                #self.account_balance = remaining_balance
                is_Successful = True

            elif Atm_simulator.remaining_balance < withdrawal_amount:
                is_Successful = False
                raise Exception('You do not have enough money for this transaction.')

        except Exception as e:
            print(str(e))

        finally:
            if (is_Successful == True):
                print('Transaction complete')
            else:
                print('Transaction Failed')
        return 

class AtmSimulatorTestCases(unittest.TestCase):

    def test_1(self):
        '''
        the first unit test tests that the program does exit if the users inputs 
        the wrong pin 3 times
        '''

        with self.assertRaises(SystemExit) as exit_exception:
            Atm_simulator.atm_entry(Atm_simulator)            
        self.assertEqual(exit_exception.exception.code, None)


    def test_2(self):
        '''
        the second unit test tests that the program proceeds to the next function if the user 
        puts the correct pin
        '''
        Atm_simulator.atm_entry(Atm_simulator)
        self.assertEqual(Atm_simulator.pin_input, Atm_simulator.pin)


    def test_3(self):
        '''
        the third unit test checks that the initial balance is 100
        '''
        Atm_simulator.atm_entry(Atm_simulator)
        self.assertTrue(Atm_simulator.account_balance == 100)

    def test_4(self):
        '''
        the fourth unit test checks that a cash withdrawal of 30 (for example) goes ahead and the remaining 
        balance is 70
        '''
        is_Successful = False
        account_balance = 100
        withdrawal_amount = 30
        if account_balance > withdrawal_amount:
                remaining_balance = account_balance - withdrawal_amount
                print('Your remaining balance is: {}'.format(remaining_balance))
                is_Successful = True
        self.assertTrue(is_Successful)

        

    def test_5(self):
        '''
        the fifth unit test checks that a cash withdrawal of more than 100 fails and you get an error message
        '''
        is_Successful = False
        account_balance = 100
        withdrawal_amount = 150
        if account_balance > withdrawal_amount:
                remaining_balance = account_balance - withdrawal_amount
                print('Your remaining balance is: {}'.format(remaining_balance))
                is_Successful = True
        self.assertFalse(is_Successful)


# calling the functions
Atm_simulator.atm_entry(Atm_simulator)
Atm_simulator.cash_withdrawal(Atm_simulator)

# running tests
print("Starting Testing")
unittest.main()
print("Ended Testing")

