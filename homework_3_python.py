# HOMEWORK WEEK 3 (Python)
#Q1
# asking for input
input_user=input('is it raining? ')
if input_user == 'y': 
    print('Take an umbrella')
elif input_user == 'n':
    print("You don't need an umbrella")
# condition for if the user inputs anything else
else:
    print("invalid input; please input only 'y' for yes and 'n' for no")

#Q2

'''
The > symbol in the if statement faces the wrong way. We want to know whether we can afford the boat 
so the if statement should be 'if my_money is greater than (so >) boat_cost' and not 'my_money is less than (<) boat_cost'
'''

# Q3

import math

def book_date_calculator():
    '''
    Calculates the century and the decade given a book dated between 1800 and 1950 but works for any
    year input. 
    book_input asks for input from the user and holds the year. 
    century divides the year by 100 to calculate the century
    decade divides the book year by 10 and multiplies by 10 to get the decade in the 70s etc format as asked.
    note: century+1 is added on the print (output variable) because the 1st century starts at 
    0 BC so 1 needs to be added otherwise for 2021 for example would output '20th' century
    '''
    book_input=int(input('What is the year the book was written? '))
    century=int(book_input/100)
    book_input=book_input-(century*100)
    decade=abs(int(book_input/10)*10)
    output=print('The book was written during the {}th century in the {}s'.format(century+1, decade))
    
    return output

# calling the function
book_date_calculator()

########### Task 2
# Q1

# The problem is the indexing: shopping_list[1] will print the 2nd item because python starts counting 
# from 0. So if we want the first item 'oranges' the correct indexing is: shopping_list[0] 

#Q2
def chocolate_price_checker():
    '''
    calculates the prices of different chocolates when inputting the chocolate type
    '''
    # asking the user for the output
    user_input=input('please input an item: ')
    
    chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
    }
    # initiating the variable to find the item 
    found=False
    
    for key in chocolates.keys():
        if user_input == key:
            price=chocolates.get(key) # to get the price
            output=('The chocolate is {} and the price is {}'.format(user_input, price))
            found=True 

    # in case the user inputs an invalud item thats not in the dictionary 
    if (found == False):
        print('Error: item not in the dictionary')

    return output

chocolate_price_checker()

#Q3

import random

def lottery_calculator():
    '''
    The programs simulates a lottery. 
    lottery_numbers are just 7 numbers for the lottery
    random_number are the random numbers to be compared with the lottery ones generated using random.sample
    '''
    lottery_numbers=[5, 7, 3, 4, 9, 2, 7] 
    random_numbers=random.sample(range(1,10),7)
    #random_numbers=[0, 0, 0, 0, 9, 0, 7] #you can use this to check if it works
    # initiating a counter that will increase if the numbers of the two lists match
    counter=0
    for number in random_numbers:
        if number in lottery_numbers:
            counter+=1

    print('You guessed {}'.format(counter))

    if counter==3:
        print('3 matching numbers: you get £20!')
    elif counter==4:
        print('4 matching numbers: you get £40!')
    elif counter==5:
        print('£5 matching numbers: you get £100!')
    elif counter==6:
        print('6 matching numbers: you get £10000!')
    elif all(number in lottery_numbers for number in random_numbers):
        print('All the numbers match: you get 1.000.000$!')
    else:
        print('You guessed less than 3 numbers correctly. There is no prize sorry!')

    return

lottery_calculator()

######### Task 3 
#Q1
'''
Pip is a package manager for python meaning that you can install python packages that are not part of the built-in packages that come with python.
Without it you would not have been able to install libraries like TensorFlow which is used for machine learning and neural networks. You 
would also not have been able to install requests which is very important for APIs. So the benefit is that you have access to a lot of libraries that 
you need. Without pip you would be very limited on what you can do in Python. One other benefit its that it is fairly easy to use and can be run from your
computer terminal
'''

#Q2
#This program should save my data to a file, but it doesn't work when I run it. What is the problem and how do I fix it?

'''
The program doesnt work because it is using 'r' instead of 'w'. r only reads the file 
so it will not write anything new in the file but w will. If you want to both read and write
then w+ has to be used
'''

#Q3
import os.path

lyrics='''
You could never know what it's like
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use
And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away
Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind
I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)
'''

with open('song.txt', 'w') as lyrics_elton_john:
    lyrics_elton_john.write(lyrics)
    # to check if the file exists/has been saved
    if os.path.isfile('song.txt'):
        print ('the file exists')
    else:
        print ('Error: the file doesn"t exist')

# to find the word i used r     
with open('song.txt', 'r') as lyrics_elton_john:
    target_word='still'
    contents=lyrics_elton_john.readlines()

    # going through the file to find the word
    for line in contents:    
        if target_word in line:
            print(line)
if target_word not in contents:
    print("word doesn't exist")


####### Task 4
#Q1
import requests 

def pokemon_id_retriever():
    '''
    Retrieves the names and moves of multiple pokemons.
    '''
    # creating a list to put the ids in
    pokemon_id_list=[]
    input_pokemon_ids=input('Please give about 6 pokemon IDs: ')
    # .split() to split the input into a list of separate items
    pokemon_id_list=input_pokemon_ids.split()
    
    with open('pokemon.txt', 'w') as pokemon_file: 
        # retrieving the api 
        for ids in pokemon_id_list:
            endpoint="https://pokeapi.co/api/v2/pokemon/{}/".format(ids)
            response=requests.get(url=endpoint)
            pokemon_json=response.json()
            # getting the pokemon name and moves
            pokemon_name=pokemon_json["name"]
            print(pokemon_name.upper())
            pokemon_moves=pokemon_json['moves']
            pokemon_file.write(pokemon_name + ':' + '\n')

            for item in pokemon_moves:
                move=item['move']
                move_name=move['name']

                # formatting the output to give . after paragraph ends and , to separate the moves
                if move_name == pokemon_moves[-1]['move']['name']:
                    pokemon_file.write(move_name + '.')
                else:
                    pokemon_file.write(move_name + ', ')
            pokemon_file.write('\n\n')
    return
