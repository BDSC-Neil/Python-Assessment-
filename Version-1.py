#Name: Neil Fernadez
#Program_Name = 91906
#Date = 28/05/23

#Function will display welcome
def greetings():
    print("Hello Welcome to the Coding Club Recruitment!!")

#Function for the Name of the Candidates
def get_string(question):
    '''chechk the input to the question is not blank'''
    user_input = ''

    while True:
        user_input = input(question)

        if not user_input.isalpha():
            print('Enter only letters pls')
            continue
        else:
            return user_input
    
#Function for age
'''chechk the input to the question is not blank and numbers only'''
def get_age(question, lowest, hightest):
    while True:
        try:
            answer = int(input(question))
            if answer >= lowest and answer <= hightest:#Limits the number from getting over 10 
                return answer
            else:
                print("Please enter your age")
        except ValueError:
            print("Please enter your age")
#Function for all nuber related question
'''chechk the input to the question is not blank and numbers only'''
def get_int(question, lowest, hightest):
    while True:
        try:
            answer = int(input(question))
            if answer >= lowest and answer <= hightest:#Limits the number from getting over 10 
                return answer
            else:
                print("Invalid number")
        except ValueError:
            print("Please enter a number")

while quit != "quit" and quit != "q":
    #Displays a greeting Message
    greetings()
    #Inputs
    #Will ask for the name of the user
    name = get_string("What is your name?: ")
    #Will ask for the last name of the user
    l_name = get_string("What is your last name?: ")
    #Will ask for the age of the user
    age = get_age("How old are you: ",1,100)
    #Will ask for the coding experience of the suer
    coding_exp = get_int("How long have you been coding: ",0,100)
    #Will ask for how many hours the user can coach
    coach_hour = get_int("How many hours can you coach in a week: ",0,100)
    #Outputs
    print("Prospect's name: {} {}".format(name,l_name))
    if age < 18 or age >30:
        #Displays if the user is under or over age
        print("Prospect's Age: {}yrs '!!Invalid Age Requirement is between 18 and 30!!'".format(age))
    elif age >= 18 or age <=30:
        #Diplays the age of the user is valid
        print("Prospect's Age: {}".format(age))
    if coding_exp >= 3:
        #Displays The user's coding experince is valid
        print("Prospect's Coding Experience: {}yrs".format(coding_exp))
    elif coding_exp < 3:
        #Displays The user's coding experince if its invalid
        print("Prospect's Coding Experience: {}yrs !!Invalid Experinece!! Requirement is more than 3yrs!!".format(coding_exp))
    if coach_hour >= 3:
        #Displays The user's coaching hours is valid
        print("Prospect's Coaching hours: {}hrs".format(coach_hour))
    elif coach_hour < 3:
        #Displays The user's coaching hours if its invalid
        print("Prospect's Coding Experience: {}yrs !!Invalid Working Hour!! Requirement is more than 3yrs!!".format(coach_hour))
    if age <= 17 or age >= 31 or coding_exp <= 2 or coach_hour <= 2:
        print("Sorry But You're Not Valid")
    else:
        print("Welcome To The Coding Club {} {}".format(name,l_name))
    #Quit option
    quit = input("Enter quit or q to stop or press any Key: ").lower()