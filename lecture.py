# Adding Special Characters to our strings
# backslash \ "escapes characters"
print("Hello \nthere!") #\n create a new line within the string
print("Hello\tThere!") # \t tabs over between chracters in string
print("This is a backslash: \\")
print("This is a really long sentence about nothing\
      i am excited to play video games this evening and sleep\
      ")
print("I called the doctor yesterday and he told me \"You need to stretch more\"")
print('My son\'s teeth are coming in and he is not sleeping')

name = "jim-bob"

spanish_string = "Quiero ir al parque mañana"

#String Concatenation
greeting = "Hello There"
name = "General Kenobi"
print(greeting + ", " + name + "!")
greeting_general = greeting + ", " + name + "!"
print(greeting_general)

# # concatenating user_input
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
# full_name = first_name + " " + last_name
# print("Hello!", full_name)
name = "Obi Wan"
name2 = "Anakin"
name3 = "Yoda"
print("Hello", "how", "are", "you", "today?")
print(name, name2, name3)

greeting = "Hello There"
name = "General Kenobi"

age = 32
print(name + " is " + str(age) + " years old")


# Customize your printed messages
# print("apple", "cherry", "banana", sep="-")

# print("This is just the beginning....", end="")
# print(" and this is the end...", end="")
# print("and here is some more stuff")

# print("chocolate chip", "moose tracks", "rocky road", sep="***", end="...yum!")

# Python formatted string
name = "Duck Guy"
duck_sentence = f"oh wow its {name}"
print(duck_sentence)

#.format()
age = 35
print("He is {} years old".format(age))

activity = "swimming"
print("He really enoys %s" % activity)

# empty strings will be falsey
empty_string = ""
# strings are immutable, they cannot be changed
# strings have no add or append method and we cannot remove from them

if empty_string:
    print(True)
else:
    print(False)

empty_string = "hello"
# similar to int(), float(), str()
# we also have bool()
is_empty = bool("hello")
print(is_empty)
print(empty_string)

# checking type of a variable --> type(variable) --> string, number
# checking if a certain variable is of a certain type --> isinstance(variable, str?)

mystery_variable = "Sherlock"
clue_list = ["candlestick", "footprint", "handkerchief"]
alleged_title = "I am a duke"
number_of_suspects = 7

# checking types
print("Typer of mystery variable: ", type(mystery_variable))
print("Number of clues found: ", len(clue_list))
print("Is the title genuine?", isinstance(alleged_title, str) )
print(isinstance(number_of_suspects, str))


# using len on a string
# len on a string - how many characters are in that string
print(len(mystery_variable))


# built-in math functions in python
import math
scores = [90.2123123, 67.3123123, 77, 89, 45 ,96]
# using python built-in functions
print(abs(-2023), round(scores[0], 2), sum(scores))
#                                               10 % 3
print(min(scores), max(scores), pow(2,3), divmod(10, 3))
#                                        floor //
print(math.sqrt(16), math.ceil(2.1), math.floor(2.9))
print(math.sin(90), math.cos(90), math.tan(90))
print(math.radians(180), math.degrees(math.pi))

"""
**Problem Statement**:
In the digital age, usernames are crucial for identity on various platforms. 
Your task is to write a program that checks if a username is neither too short nor too long, 
adhering to specific length criteria.

**Instructions**:

1. Prompt the user to enter a username.
2. Check if the username is between 5 and 15 characters long.
3. If the username meets the criteria, print a confirmation message.
4. If it does not meet the criteria, print a message indicating the username length requirements.
5. Provide the user with the option to try a different username or exit the program.

**Hints**:

- Use the `len()` function to determine the length of the username.
- Use an `if-else` statement to check if the username's length falls within the specified range.
- You'll need a while loop to drive the options.

"""



# choice = True
# while choice:
#     username = input("Enter a username: ")
#     if len(username) >= 5 and len(username) <= 15:
#         print("Username is valid")
#         break
#     else:
#         print("Username must be between 5 and 15 characters long. Try again.")
#         choice = input("Do you to continue trying different username? (yes/no): ")
#         if choice == "no":
#             choice = False



# username = ""
# while not username:
#       username = input("Enter your desired username: ")
#       if username == "exit":
#            break
#       elif len(username) < 5 or len(username) > 15:
#            username = ""
#            print("Please enter a username between 5 and 15 characters. Or enter 'exit' to quit.")
#       else:
#            print(f"Your new username is {username}")


# while True:
#       user_input = input("create a username: Say 'quit' to quit.")
#       if 5 < int(len(user_input)) <= 15:
#             print("your username is valid")
#             break
#       if user_input == 'quit':
#             break
#       else:
#             print("your username is not valid")

# Built in String Functions for python
#find() - return the position of the first occurence in a string
alphabet = "abcdefghijkljmnjojpqjrjstujvwxjyz"
found_position = alphabet.find('j')
print(found_position)

# replace() is going to replace a specific phrase or character in the string
# with another phrase
#.replace(oldvalue, newvalue, count)
sentence = "I have been watching Dragon Ball Z. It is really cool. They collected Dragon Balls. And also Dragon. Dragon again"
new_sentence = sentence.replace("Dragon", "Kitten")
print(new_sentence)

# .strip() removes whitespace from all sides of a string
my_string = "           Hello there        "
print(my_string)
stripped_string = my_string.strip()
print(stripped_string)

# .count() -> returns the number of occurences of a specific character or phrase
sentence = "I have been watching Dragon Ball Z. It is really cool. They collected Dragon Balls. And also Dragon. Dragon again"
dragon_count = sentence.count("Dragon")
print(dragon_count)

# .startswith() -> returns a boolean depending if the string starts with the passed in character or phrase
greeting = "Hello there"
starts = greeting.startswith('Hello')
print(starts)
starts_again = greeting.startswith('H')
print(starts_again)

# .endswith() -> returns a boolean depending if the string ends with the passed in character or phrase
greeting = "Hello there"
ends = greeting.endswith("there")
print(ends)

# isalpha() -> if all characters in a string are letters
robot = "R2D2"
letter_bot = robot.isalpha()
print(letter_bot)
robot2 = "MegaMan"
letter_bot2 = robot2.isalpha()
print(letter_bot2)

# isdigit() checks if all characters are digits
serial_number = "157264913827140"
is_digit = serial_number.isdigit()
print(is_digit)

# isspace() check if all characters are whitespace
whitespace = "                   "
is_space = whitespace.isspace()
print("no variable", whitespace.isspace())
# print(is_space)

# zfill() fills a string with however many 0's you tell it
number = '50'
x = number.zfill(10)
print(x)

# ========== PYTHON FUNCTIONS ================
# creating a python function
# def keyword function name()
def function_name():
    pass # pass so i dont get indentation errors down the line
# just like with variables, functions can be called whatever we want them to be
# BUT they should be named somethign relevant to what theyre doing

def greet_user():
    print("HELLO, USER!")

# calling our function
# call the function by typing the function name followed by parentheses
greet_user() # <- parentheses tell the interpreter the function is being called

# adding function parameters
# paremeter is a variable placeholder than a function acts on
               # paremeters go here  - parameter is a place holder for the argument           
def greet_user1(username):
    print(f"Hello, {username}")

# calling a function with a argument
# argument goes in the parentheses when we call a function
greet_user1('Coolguy420lmao')
greet_user1('Rhoadehouse')
greet_user1('360noscope')
greet_user1('hiyuhh')

my_name = "anotherusername"
username = "yoloswag4jesus"
greet_user1(my_name)
greet_user1(username)

def greeting():
    username = input("Hello! Please enter your username")
    print(f"Hello there, {username}")
# greeting()

def game_greeting(game):
    username = input("Hello! Please enter your username")
    print(f"Hello {username}! Have a nice time playing {game}")

# game_greeting('Super Smash Brothers Ultimate')
# game_greeting("Valorant")

def fav_games(game1, game2):
    print(f"My two favorite games are: {game1} and {game2}")

fav_games('Silver Version', "Fire Emblem Sacred Stones")


# default parameters def function(param=value)
def brew_coffee(size="medium"):
    print(f"Brewing a {size} coffee")

brew_coffee() # This will print "Brewing a medium coffee" because it takes the default parameter
brew_coffee('large') # "Brewing a large coffee" because the argument provided overwrites the default parameter

# default parameters MUST follow non-default parameters
def get_breakfast(breakfast, drink="coffee"):
    print(f"I am eating {breakfast} for breakfast and enjoying a nice {drink}.")

get_breakfast("Toaster Strudel")   # calling without an argument for drink so it takes the default
get_breakfast("Cherry Pie", "glass of milk") # calling with an argument to overwrite our default parameter


# Looping with functions
flavors = ["chocolate", "vanilla", "pistachio", "mint chocolate chip", "moose tracks"]
def scoop_icecream(alist):
    scoop_counter = 0
    while scoop_counter < len(alist):
        print(alist[scoop_counter])
        scoop_counter += 1
scoop_icecream(flavors)
valorant_agents = ["Jett", "Omen", "Breach", "Kayo", "Reyna", "Sage"]
scoop_icecream(valorant_agents)
pokemon = ["Heracross", "Espeon", "Crobat", "Bayleaf", "Eevee", "Scyther", "Diglet", "Charizard", "Mew" ]
scoop_icecream(pokemon)

# *args and **kwargs
# *parameter name, lets our function take in any number of arguments
def video_game_characters(*characters):
    print(characters)
    for name in characters:
        print(name)
video_game_characters("Cypher", "Pew Pew Guy", "Pikachu", "Lynn", "Mega Man", "Boba Fett", "Tom Nook", "Sheldon", "Mario", "Link", "Diglet")


# **kwargs
#keyword argument keyword(variable) = somevalue
def make_sandwich(**ingredients):
    print(ingredients)
#     using dict.items()
    for item, quantity in ingredients.items():
        print(f"Adding {quantity} of {item} to the sandwich ")

make_sandwich(tomatoes="3 slices", lettuce="2 leaves", mayo="1 small scoop", pickles = "3 chips")

# single keyword arguments
def game_characters(**characters):
    print(characters)
    for game, character in characters.items():
        print(f"{character} is from {game}")
    

game_characters(Valorant = "Cypher", Super_Mario = "Mario", Legend_of_Zelda="Link")
#                 key   :    value        key        value        key            value

characters = {'Valorant': 'Cypher', 'Super_Mario': 'Mario', 'Legend_of_Zelda': 'Link'}
print(characters.items())

# returning from functions
# return will be the last thing a function does before it ends
# an output that we can use and manipulate, set to a variable or pass into other functions
def add_numbers(a, b):
#     print(a + b)
    
    return a + b

# printing fucntion output so we can see it in the terminal
print(add_numbers(5, 9))

# setting a return value to a variable
result = add_numbers(6,20)
print(result)

def sum_list(alist):
    return sum(alist)

print(sum_list([1,2,3,4,5]))

# conditionals in functions -- multiple returns
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = check_even(5) 
print(result)

# def get_username():
#       username = input("Please enter your username! ")
#       return username
# my_username = get_username()
# print(f"My username is {my_username}")

def show_details():
    name = "Ryan"
    age = 32
    return name, age
print(show_details())
person_name, person_age = show_details() # ('Ryan', 32)

print(person_name, person_age)


# Scoping 
# setting a variable all the way to the left, makes that variable global
global_variable = "The world"
#anywhere underneath this ^ variable has access to it

def print_world():
#     accessing a global variable within a function
    print(global_variable)
print_world()

# creating a function with a variable scoped to that function
def greet():
    #function scoped variable
    message = "Wear sunscreen!"
    print(message)
#we cannot access a variable scoped to our function outside of the function
# print(message)

name = "Alice"

def introduce():
    name = "Bob"
    print(f"Hello my name is {name}")
introduce()
print(name)

# pass with a function
def do_something():
    #not quite sure what to do with my function yet
    pass

# global list variable
my_stuff = []

def add_shirt():
    while True:        
      thing = input("What shirt would you like to add to your stuff? ")
      if thing == "quit":          
          break
      my_stuff.append(thing)

def add_game():
    while True:
      game = input("What game would you like to add to your stuff?")
      
      if game == "quit":
          break
      my_stuff.append(game)

def add_food():
    while True:
      food = input("What food would you like to add to your stuff?")
      if food == "quit":
          break
      my_stuff.append(food)
def show_stuff():
    print("Heres all your stuff: ")
    for stuff in my_stuff:
        print(stuff)

# add_shirt()
# add_game()
# add_food()
# show_stuff()
        

"""
**Problem Statement**:
You are developing a feature for a music app that allows users to create a custom playlist and play the songs in sequence.

**Instructions**:

1. Define a function called `play_songs()` that takes one parameter `song_list`.
2. Inside the function, use a loop to iterate over `song_list`.
3. For each song in the list, print a message indicating that the song is now playing.
4. Before calling the function, prompt the user to enter the number of songs they want to add to the playlist.
5. Use a loop and `input()` to accept song names from the user, based on the number they provided, and store them in a list.
6. Call the `play_songs()` function with the user-created list of songs as an argument.
"""

        

def play_songs(song_list):
    for song in song_list:
       print(f"\nNow Playing: {song}")

# playlist = []
# num_songs = int(input("\nEnter the number of songs you want in your playlist: "))

# for i in range(num_songs):
#     song_name = input(f"\nEnter song name {i+1}: ")
#     playlist.append(song_name)

# play_songs(playlist)
# print()

# def play_songs(song_list):
#     for song in song_list:
#         print(f"now playing, {song}")
# num_songs=int(input("Enter the number of songs you want to add to the playlist: "))
# song_list=[]
# for i in range(num_songs):
#     song_name= input("Enter the name of song {}:".format(i+1))
#     song_list.append(song_name)
    

# play_songs(song_list)
    


# playlist = []
# def play_songs(song_list):
#     while True:
#         user_choice = input("Add your song: type 'quit' to quit. ")
        
#         if user_choice == "quit":
#             break
#         playlist.append(user_choice)
#         print(playlist)
# def current_playlist():
#     print("Your current playlist:")
#     for songs in playlist:
    
#         print(songs)
# play_songs(playlist)
# current_playlist()
    

# song_list = []
# def play_songs():    
    
#     while True:
#         song = input("What would you like to listen to? ")
#         if song == "done":
#             break
#         song_list.append(song)
#         print(f"{song} is now added to the queue!")

# print
# play_songs()
# for song in song_list:
#     print(f"Now playing: {song}")


import pdb

def add_numbers(num):
      total = 0
      for i in range(num):
            # pdb.set_trace() # sets a breakpoint in the code so i can start checking line by line
            total += i
            print(f"{i} + {total}")
            print(total)
      return total
print(add_numbers(5))




