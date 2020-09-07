# Functions
from email.utils import *  # this line will make all functions inside the utils module(in the email package) available in current file

import time

COMPANY = "Level Up"


# Defining the functions
def greet_user():
    """Greets the user."""
    print("Welcome to Class!")
    print("this was basic function")


def greet_user_1(name):
    """Greeting the user with given name."""
    print(f"Welcome to {name}!")


def greet_user_2(company, username):
    """Greeting the user with given name."""
    print(f"{username.title()}, Welcome to {company.upper()}!")
    print("Have a Great Week!")


# company argument is an optional argument(keyword), and default value is 'google'
def greet_user_3(username, company="google"):
    """Greeting the user with given username and keyword argument 'company'."""
    print(f"{username.title()}, Welcome to {company.upper()}!")
    print("Have a Great Week!")


# company argument is an optional argument(keyword), and with no default value
def greet_user_4(username, company=None):
    """Greeting the user with given username and keyword argument 'company'."""
    if company is None:
        print(f"{username.title()}, Welcome to new Home!")
    else:
        print(f"{username.title()}, Welcome to {company.upper()}!")
    print("Have a Great Week!")
    greet_user()

    def hello_world():
        print("hello world")

    hello_world()


def add_inc(name):
    print(f"your company name: {COMPANY}")
    print(f"{name} Inc.")
    # COMPANY = COMPANY + 'Inc.'


# print("EXECUTION OF FUNCTIONS")
# comp = 'Level Up'
# greet_user()  # this is the execution of the code inside the functions >> calling the function
# time.sleep(5)
#
# greet_user_1("Jungle")  # name parameter is required here, otherwise TypeError is thrown
# greet_user_1(comp)  # name parameter is required here, otherwise TypeError is thrown
#
# greet_user_1(input('enter company name: '))

# Package - directory with '__init__.py' empty file
# Module - '.py' file (python file)

# greet_user_2('levelup', 'Rustem')
# greet_user_2('Rustem', 'Google')  # position is important here to print or do the execution correctly
# # greet_user_2('Rustem') # TypeError: greet_user_2() missing 1 required positional argument: 'username'
# greet_user_3('Polina')  # here function is using default value for company argument, which was not provided in the call
# greet_user_3('Abdul', 'Facebook')  # function overwrites the default 'google' value for the company argument


greet_user_4('Vika')  # company argument was not used, see the if condition in the function
greet_user_4('Murod', 'Bloomberg')
greet_user_4(company='Bloomberg', username='Murod')

# HW: from 8-1 to 8-5
