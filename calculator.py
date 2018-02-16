"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator():

    while True:

        print "Welcome to your prefix calculator"
        print "Your options are to add, subtract, multiply, divide... q to quit"
        input = raw_input("Please enter a string to compute: ")

        tokens = input.split(" ")

        if tokens[0] == "q":
            break

        if tokens[0] == "add":
            sum = add(int(tokens[1]), int(tokens[2]))
            print "The sum of {} and {} is {}".format(tokens[1], tokens[2], sum)

        if tokens[0] == "subtract":
            diff = subtract(int(tokens[1]), int(tokens[2]))
            print "The difference of {} and {} is {}".format(tokens[1], tokens[2], diff)

        if tokens[0] == "divide":
            div = divide(int(tokens[1]), int(tokens[2]))
            print "If you divide {} by {} you have {}".format(tokens[1], tokens[2], div)

        if tokens[0] == "square":
            sq = square(int(tokens[1]))
            print "The square of {} is {}".format(tokens[1], sq)
        
        if tokens[0] == "cube":
            cu = cube(int(tokens[1]))
            print "The cube of {} is {}".format(tokens[1], cu)

        if tokens[0] == "power":
            pow = power(int(tokens[1]), int(tokens[2]))
            print "The {} to the power of {} is {}".format(tokens[1], tokens[2], pow)

        if tokens[0] == "mod":
            modulo = mod(int(tokens[1]), int(tokens[2]))
            print "The mod of {} and {} is {}".format(tokens[1], tokens[2], modulo) 


calculator()
