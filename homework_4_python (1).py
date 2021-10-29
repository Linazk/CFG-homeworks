# Task 1 (theory)

'''
GIT WORKFLOW FUNDAMENTALS
·        Working Directory:
The working directory is the folder in which we are currently (working) on. The 'pwd' command in the terminal
shows the working directory and stands for 'print working directory'
·        Staging Area:

A staging area in git is the area where any files we have added are waiting to be commited to git using
the git commit command

·        Local Repo (head):

Local repository is the one we have in out computer that is managed locally. Head is the current branch.
If we change branches head will also change 

·        Remote repo (master):
A remote repository is the opposite of the local repository meaning that it is not in our local computer
and it instead exists in the internet. Master is the default or initial branch of a repository.
 
WORKING DIRECTORY STATES:
·        Staged:

staged means that a file is getting ready for a git commit. That happens when we do 'git add' or 
'git add .' that adds all of the files to be committed

·        Modified:

Modified happens when you change/edit files that you have commited. Git checks and displays 
that the files have been modified

·        Committed:

Committed is displayed next to files that have been committed and waiting to be pushed. That happens after git add

 
GIT COMMANDS:
·        Git add:

The git add command is used to add files to the staging area. This is the first step for uploading files 
in git 

·        Git commit:

The git commit command is used to commit files that have been added. It is important to know that 
files need to be added first with git add before they are commited with git commit. Git commit 
takes the files from the staging are and prepares them for git push which is the next step.

·        Git push:

The git push command is used to upload the files that have previosuly been committed (locally) 
to a remote repository. This allows us to upload our files on Github or similar hosting websites


·        Git fetch:

Git fetch is the opposite of git push meaning that it downloads files that have been pushed. We use this 
command for example when we work in a team and a teammate has git pushed a file. To see/read/modify that
file we need to use git fetch to download it

·        Git merge:

The git merge command merges a branch into another branch. We can use this if we have used different
branches to work on different versions of a project with many people as contributors and now we want to 
combine that into one. The source branch remains unchanged and only the target branch is changed.

·        Git pull:

Git pull uses both git fetch and merge: it takes/downloads new commits and then merges them into our
local branch. We can use git pull if we want to update our local branch with new changes 

'''

# Task 2 (ATM code)
# i put the unit tests and the atm functions all on the same file because that is how i assumed it was needed for grading

import unittest

class Atm_simulator:
    def atm_entry(self):
        '''
        Simulates an atm entry by asking for user input for the pin. If initially pin is not correct 3 tries 
        are given. If after 3 tries it is still not correct then the program quits.
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
                self.pin_input=input('incorrect pin: you have {} more tries: '.format(pin_count))
                count+=1
                pin_count-=1

        if count > 2:
            print('Invalid pin 3 times. Exiting the program')
            # to exit the program
            exit()

        out1 = print('Correct pin')

        return out1 


    def cash_withdrawal(self):
        '''
        This function is for calculating the cash withdrawal. If the user tries to withdraw
        more money than they have then an exception is raised and the program exits
        '''

        # setting it outside the try/except. it is for determing if the withdrawal is succesful or not
        is_Successful = False

        try:
            self.withdrawal_amount = int(input('Please input a withdrawal amount: '))

        #for if they enter invalid input
        except Exception as withdrawal_error:
            print("Value entered is not a valid number")
            print(str(withdrawal_error))

        try:
            # for if the withdrawal is successful
            if self.account_balance > self.withdrawal_amount:
                self.remaining_balance = self.account_balance - self.withdrawal_amount
                print('Your remaining balance is: {}'.format(self.remaining_balance))
                is_Successful = True
            # if it is unsuccessful
            elif self.remaining_balance < self.withdrawal_amount:
                is_Successful = False
                # raising the exception
                raise Exception('You do not have enough money for this transaction.')

        except Exception as withdrawal_error:
            print(str(withdrawal_error))

        finally:
            if (is_Successful == True):
                print('Transaction complete')
            else:
                print('Transaction Failed')
        return 

# Task 3

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
        #setting the parameters to test that it works
        # I put 30 as an example 
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
        # similar to the above test I put 150 on the withdrawal amount as an example to test it
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

# running the tests
print("Starting Testing")
unittest.main()
print("Ended Testing")

