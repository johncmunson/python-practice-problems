# ██████  ██    ██ ████████ ██   ██  ██████  ███    ██
# ██   ██  ██  ██     ██    ██   ██ ██    ██ ████   ██
# ██████    ████      ██    ███████ ██    ██ ██ ██  ██
# ██         ██       ██    ██   ██ ██    ██ ██  ██ ██
# ██         ██       ██    ██   ██  ██████  ██   ████

# ██████  ██████   █████   ██████ ████████ ██  ██████ ███████
# ██   ██ ██   ██ ██   ██ ██         ██    ██ ██      ██
# ██████  ██████  ███████ ██         ██    ██ ██      █████
# ██      ██   ██ ██   ██ ██         ██    ██ ██      ██
# ██      ██   ██ ██   ██  ██████    ██    ██  ██████ ███████

# ██████  ██████   ██████  ██████  ██      ███████ ███    ███ ███████
# ██   ██ ██   ██ ██    ██ ██   ██ ██      ██      ████  ████ ██
# ██████  ██████  ██    ██ ██████  ██      █████   ██ ████ ██ ███████
# ██      ██   ██ ██    ██ ██   ██ ██      ██      ██  ██  ██      ██
# ██      ██   ██  ██████  ██████  ███████ ███████ ██      ██ ███████

# https://www.practicepython.org/

# ##############################################################################


#  ██████   ██
# ██  ████ ███
# ██ ██ ██  ██
# ████  ██  ██
#  ██████   ██  Character Input

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will
# turn 100 years old. Bonus: Ask how many times the user would like for their
# message to be printed out.

# import datetime
#
# name = input('What\'s your name? ')
# age = int(input('What\'s your age? '))
# times_to_print = int(input('How many times do you want to know your centennial year? '))
# centennial = datetime.datetime.now().year + (100 - age)
# message = '{name}, you will turn 100 years old in the year {centennial}.'.format(name = name, centennial = centennial)
#
# for i in range(0, times_to_print):
#     print(message + '\n')


#  ██████  ██████
# ██  ████      ██
# ██ ██ ██  █████
# ████  ██ ██
#  ██████  ███████  Odd or Even

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Bonus: If the number is a
# multiple of 4, print out a different message. Bonus: Ask the user for two
# numbers: one number to check (call it num) and one number to divide by
# (check). If check divides evenly into num, tell that to the user. If not,
# print a different appropriate message.

# number = int(input('Enter a number: '))
# isEven = number % 2 == 0
# if isEven:
#     print('The number is even.')
# else:
#     print('The number is odd.')


#  ██████  ██████
# ██  ████      ██
# ██ ██ ██  █████
# ████  ██      ██
#  ██████  ██████  List Less Than Ten

# Take a list, this one for example: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
# and write a program that prints out all the elements of the list that are less
# than 5. Bonus: Instead of printing the elements one by one, make a new list
# that has all the elements less than 5 from this list in it and print out this
# new list. Bonus: Write this in one line of Python. Bonus: Ask the user for a
# number and return a list that contains only elements from the original list a
# that are smaller than that number given by the user.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for num in a:
#     if num < 5:
#         print(num)


#  ██████  ██   ██
# ██  ████ ██   ██
# ██ ██ ██ ███████
# ████  ██      ██
#  ██████       ██  Divisors

# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. (If you don’t know what a divisor is, it is a
# number that divides evenly into another number. For example, 13 is a divisor
# of 26 because 26 / 13 has no remainder.)

# num = int(input('Enter a number: '))
#
# def get_divisors(num):
#     divisors = []
#     for n in range(1, num + 1):
#         if num % n == 0:
#             divisors.append(n)
#     return divisors
#
# print(get_divisors(num))


#  ██████  ███████
# ██  ████ ██
# ██ ██ ██ ███████
# ████  ██      ██
#  ██████  ███████  List Overlap

# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program
# works on two lists of different sizes. Bonus: Randomly generate two lists to
# test this. Bonus: Write this in one line of Python.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# joined = a + b
#
# unique = list(set(joined))
#
# print(unique)


#  ██████   ██████
# ██  ████ ██
# ██ ██ ██ ███████
# ████  ██ ██    ██
#  ██████   ██████  String Lists

# Ask the user for a string and print out whether this string is a palindrome or
# not. (A palindrome is a string that reads the same forwards and backwards.)

# def reverse_str(str):
#     rev = str[::-1] # alternatively... rev = ''.join(reversed(str))
#     return rev
#
# def is_palindrome(str):
#     str = str.lower()
#     reversed_str = reverse_str(str)
#     if str == reversed_str:
#         return True
#     else:
#         return False
#
# input = input('Enter a string and I will tell you if it is a palindrome or not... ')
#
# if is_palindrome(input):
#     print('Yes, that is a palindrome.')
# else:
#     print('No, that is not a palindrome.')


#  ██████  ███████
# ██  ████      ██
# ██ ██ ██     ██
# ████  ██    ██
#  ██████     ██  List Comprehensions

# Let’s say I give you a list saved in a variable:
#   a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write one line of Python that takes this list a and makes a new list that has
# only the even elements of this list in it.

# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# evens = [n for n in numbers if n % 2 == 0]
# print(evens)


#  ██████   █████
# ██  ████ ██   ██
# ██ ██ ██  █████
# ████  ██ ██   ██
#  ██████   █████  Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using
# input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# p1_score = 0
# p2_score = 0
#
# while True:
#     p1_attack = input('P1, enter rock, paper, or scissors: ')
#     p2_attack = input('P2, enter rock, paper, or scissors: ')
#
#     if (
#         (
#             p1_attack != 'rock'
#             and p1_attack != 'paper'
#             and p1_attack != 'scissors'
#         ) or (
#             p2_attack != 'rock'
#             and p2_attack != 'paper'
#             and p2_attack != 'scissors'
#         )
#     ):
#         print('Invalid Input, try again.')
#     elif p1_attack == p2_attack:
#         print('Draw!')
#     elif p1_attack == 'rock':
#         if p2_attack == 'scissors':
#             print('P1 Wins!')
#             p1_score += 1
#         else:
#             print('P2 Wins!')
#             p2_score += 1
#     elif p1_attack == 'paper':
#         if p2_attack == 'rock':
#             print('P1 Wins!')
#             p1_score += 1
#         else:
#             print('P2 Wins!')
#             p2_score += 1
#     else:
#         if p2_attack == 'paper':
#             print('P1 Wins!')
#             p1_score += 1
#         else:
#             print('P2 Wins!')
#             p2_score += 1
#
#     print('''The current score is...
#         P1: {}
#         P2: {}'''.format(p1_score, p2_score))
#
#     play_again = input('Play again? (y/n): ')
#
#     if play_again == 'n':
#         if p1_score == p2_score:
#             print('The game ended in a draw!')
#         elif p1_score > p2_score:
#             print('P1 wins the game!')
#         else:
#             print('P2 wins the game!')
#         break


#  ██████   █████
# ██  ████ ██   ██
# ██ ██ ██  ██████
# ████  ██      ██
#  ██████   █████  Guessing Game One

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or
# exactly right. (Hint: remember to use the user input lessons from the very
# first exercise). Bonus: Keep the game going until the user types “exit”.
# Bonus: Keep track of how many guesses the user has taken, and when the game
# ends, print this out.

# import random
#
# number = random.randint(1, 9)
# guesses = 0
#
# print('Guess a number between 0 and 10.')
#
# while True:
#     guesses += 1
#     guess = int(input('What\'s your guess? '))
#     if guess == number:
#         print('Correct! It took you this many attempts: {}'.format(guesses))
#         break
#     elif guess < number:
#         print('Too low')
#     else:
#         print('Too high')


#  ██  ██████
# ███ ██  ████
#  ██ ██ ██ ██
#  ██ ████  ██
#  ██  ██████  List Overlap Comprehensions

# This week’s exercise is going to be revisiting an old exercise (see Exercise
# 5), except require the solution in a different way. Take two lists, say for
# example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program
# works on two lists of different sizes. Write this using at least one list
# comprehension. (Hint: Remember list comprehensions from Exercise 7).
# Bonus: Randomly generate two lists to test this.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# def find_unique(list1, list2):
#     # For the list comprehension below to work, the initial lists must not
#     # contain duplicates within themselves. We could remove duplicates several
#     # ways. A set would work, but we'll try using a dict this time. This works
#     # because dicts cannot have duplicate keys. Note: this challenge was focused
#     # on list comprehensions, but the easiest way to solve this would've been
#     # to concatenate the lists and then use set()
#     list1 = list(dict.fromkeys(list1))
#     list2 = list(dict.fromkeys(list2))
#
#     unique = [i for i in a if i in b]
#
#     return unique
#
# print(find_unique(a, b))


#  ██  ██
# ███ ███
#  ██  ██
#  ██  ██
#  ██  ██  Check Primality Functions

# Ask the user for a number and determine whether the number is prime or not.
# You can (and should!) use your answer to Exercise 4 to help you. Take this
# opportunity to practice using functions, described below.

# Note: be sure to uncomment the get_divisors function from problem 4 when
# running the code below.

# num = int(input('Enter a number to see if it is prime or not: '))
#
# def is_prime(num):
#     divisors = get_divisors(num)
#     if len(divisors) == 2:
#         return True
#     return False
#
# if is_prime(num):
#     print('Yes, that is a prime number.')
# else:
#     print('No, that is not a prime number.')


#  ██ ██████
# ███      ██
#  ██  █████
#  ██ ██
#  ██ ███████  List Ends

# Write a program that takes a list of numbers and makes a new list of only the
# first and last elements of the given list. For practice, write this code
# inside a function.

# a = [5, 10, 15, 20, 25]
#
# # Option 1: List comprehension
# def first_last_1(list):
#     new_list = [n for i, n in enumerate(list) if i == 0 or i == len(list) - 1]
#     return new_list
#
# # Option 2: Square brackets
# def first_last_2(list):
#     first = list[0]
#     last = list[-1]
#     return [first, last]
#
# print('Option 1: ' + str(first_last_1(a)))
# print('Option 2: ' + str(first_last_2(a)))


#  ██ ██████
# ███      ██
#  ██  █████
#  ██      ██
#  ██ ██████  Fibonacci

# Write a program that asks the user how many Fibonnaci numbers to generate and
# then generates them. Take this opportunity to think about how you can use
# functions. Make sure to ask the user to enter the number of numbers in the
# sequence to generate.

# def fibonacci(length = 10):
#     sequence = [1, 1]
#     while len(sequence) != length:
#         sequence.append(sequence[-2] + sequence[-1])
#     return sequence
#
# print(fibonacci(30))


#  ██ ██   ██
# ███ ██   ██
#  ██ ███████
#  ██      ██
#  ██      ██  List Remove Duplicates

# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.
# Bonus: Write two different functions to do this - one using a loop and
# constructing a list, and another using sets. Bonus: Go back and do Exercise 5
# using sets, and write the solution for that in a different function.

# from random import randrange
#
# random_numbers = [randrange(10) for i in range(25)]
#
# # Option 1: loop
# def dedupe_1(arr):
#     unique_numbers = []
#     for num in arr:
#         if num not in unique_numbers:
#             unique_numbers.append(num)
#     return unique_numbers
#
# # Option 2: set
# def dedupe_2(arr):
#     return list(set(arr))
#
# print('Option 1: ' + str(dedupe_1(random_numbers)))
# print('Option 2: ' + str(dedupe_2(random_numbers)))


#  ██ ███████
# ███ ██
#  ██ ███████
#  ██      ██
#  ██ ███████  Reverse Word Order

# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string, except with
# the words in backwards order. For example, say I type the string:
#   My name is Michele
# Then I would see the string:
#   Michele is name My
# shown back to me.

# sentence = input('Enter a sample sentence to reverse the word order: ')
#
# def sentence_reverser(sentence):
#     tokens = sentence.split()
#     reversed_tokens = tokens[::-1]
#     reversed_sentence = ' '.join(reversed_tokens)
#     return reversed_sentence
#
# print(sentence_reverser(sentence))


# ██████  ██   ██
#      ██ ██   ██
#  █████  ███████
# ██           ██
# ███████      ██  Draw A Game Board

# Time for some fake graphics! Let’s say we want to draw game boards that look
# like this:
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other
# sizes (8x8 for chess, 19x19 for Go, and many more). Ask the user what size
# game board they want to draw, and draw it for them to the screen using
# Python’s print statement.

rows = int(input('How many rows for your game board? '))
columns = int(input('How many columns for your game board? '))

def get_horizontal_line(columns):
    line = ''
    for i in range(1, columns + 1):
        line += '--- '
    line = ' ' + line
    return line

def get_vertical_line(columns):
    line = ''
    for num in range(1, columns + 1):
        line += '|   '
    line = line + '|'
    return line

for i in range(1, (rows * 2) + 2):
    if i % 2 == 0:
        print(get_vertical_line(columns))
    else:
        print(get_horizontal_line(columns))
