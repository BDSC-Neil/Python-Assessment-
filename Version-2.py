#Name: Neil Fernadez
#Program_Name =  91906-v.2
#Date = 19/06/23

import sys

#Function will display welcome
def greetings():
    print("Welcome to the Coding Club ")

#Function for the Name of the Candidates
def get_string(question):
    '''check that the input to the question is not blank and contains only letters'''
    while True:
        user_input = input(question)

        if not user_input.isalpha():
            print('Enter only letters')
        else:
            return user_input

#Function for age
def get_age(question, lowest, highest):
    while True:
        try:
            answer = int(input(question))
            if answer < lowest or answer > highest:
                print("Age allowed is between {} and {} years old".format(lowest, highest))
                sys.exit() #This is so when the age is invalid the program will force to stop thats why I imported sys
            return answer
        except ValueError:
            print("Please enter your age as a valid number.")
#Function for all nuber related question
def get_int(question, lowest, highest):
    while True:
        try:
            answer = int(input(question))
            if answer < lowest or answer > highest:#Limits the number from getting over 10 
                print("Invalid amount, allowed is between {} and {}".format(lowest, highest))
                sys.exit() #This is so when the age is invalid the program will force to stop thats why I imported sys
            return answer
        except ValueError:
            print("Please enter a number")

while quit != "quit" and quit != "q":
    greetings()
    #Inputs
    name = get_string("What is your first name?: ")
    l_name = get_string("What is your last name?: ")
    x = get_age("How old are you: ",18,30)
    y = get_int("How long have you been coding: ",3,100)
    z = get_int("How many hours can you coach in a week: ",3,100)
    #Outputs
    print("Prospect's name: {} {}".format(name,l_name))
    print("Prospect's Age: {}".format(x))
    print("Prospect's Coding Experience: {}yrs".format(y))
    print("Prospect's Coaching hours: {}hrs".format(z))
    print("Congrats, {} {} you are valid to enter the Coding Club!!".format(name,l_name))
    #Q
    quit = input("Enter quit or q to stop or press any Key: ").lower()

