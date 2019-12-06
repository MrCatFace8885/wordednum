#!/usr/bin/env python3
'''This is a program that simply converts an integer to worded form. It is run as a command line utility.
I plan on adding support for floating point numbers in the future.
#Written by MrCatFace8885'''

version = "1" #revision number of this program.

from sys import argv,stderr #Importing this stuff allows reading command arguments, and outputting to stderr.
from math import floor #I love floors

def print_version(): #Function that prints the version number of the program and then terminates it.
    print("wordednum, revision " + version + "\nWritten by MrCatFace8885")
    exit()


def parse_args(): #Function that handles optional arguments.
    args_given = [] #Stores the arguments passed by the user.

    shorthands = {"v":"version"} #Aliases for the args, called shorthands, are here.
    args_allowed = ["version"]

    for arg in numbers: #Getting the longhand and shorthand args.
        if arg[0:2] == "--":
            if arg[2:] in args_allowed:
                args_given.append(arg[2:])

            else:
                print("\033[1;31merror:\033[0m Invalid argument: " + arg,file=stderr)
                exit(2)

        elif arg[0] == "-" and not arg[1:].isdigit(): #I have no idea what I'm doing
            for x in arg[1:]:
                try:
                    args_given.append(shorthands[x])
                except KeyError:
                    print("\033[1;31merror:\033[0m Invalid argument: -" + x,file=stderr)
                    exit(2)

    if "version" in args_given: #If the --version argument is passed, print the program's version.
        print_version()


def convert_num(n): #Function that converts a single number into a string of its worded form.
    if int(n) == 0:
        return "zero"

    retval = "" #Declaring the string for the return value.

    if n[0] == "-": #If n is negative, append "negative " to retval and remove the - from n.
        retval += "negative "
        n = n[1:]

    while n[0] == "0": #Removing the leading zeros from n.
        n = n[1:]

    while len(n) % 3: #Adding some 0's back to make the string length divisable by 3. This makes things easier to code.
        n = "0" + n
    illions = floor(len(n) / 3) #I'm using the term "illions," because I forgot the real term for it.

    illion_counter = illions #This variable acts as a counter for the segment it's on. This feels redundant, and I hate it.
    for x in range(illions): #This loop does the magic of converting the number to worded form.
        seg = n[x * 3:x * 3 + 3]

        if seg == "000": #If the segment is all 0's, don't do anything. Just move on to the next segment.
            illion_counter -= 1
            continue

        #Converting the first digit of a segment.
        if seg[0] != "0":
            retval += phrases.uno[int(seg[0])] + " hundred"

        #Converting the second and third digits of the segment.
        if int(seg[1:]) >= 20:
            if seg[0] != "0":
                retval += " "
            retval += phrases.dos[int(seg[1])]
            if seg[2] != "0":
                retval += "-" + phrases.uno[int(seg[2])]

        elif seg[1:] != "00": #If the last two digits is less than 20 and not 0, this code is run instead.
            if seg[0] != "0":
                retval += " "
            retval += phrases.uno[int(seg[1:])]

        #Adding the correct "illion" word.
        if illion_counter - 1 == 0: #Do nothing if on the last segment.
            pass
        elif illion_counter - 1 == 1: #If on the second-to-last segment, print "thousend."
            retval += " thousand"
        else:
            try:
                retval += " " + phrases.illion[illion_counter - 3] + "illion"
            except IndexError:
                print("\033[1;31merror:\033[0m One of the numbers inputted is too long! I can only go up to duodecillion",file=stderr)
                exit(1)

        if illion_counter > 1: #This if statement appends a space if it's not on the last segment.
            retval += " "

        illion_counter -= 1

    return retval



'''The "logic" of this program is contained in here. The function returns a single string of
all the numbers in array numbers in worded form. The numbers in the output are split with
newline characters.'''
def main():
    global numbers #Hey guys, this dude is using global variables, that's so cringe man
    global phrases

    retval = "" #Declaring an empty string. This string acts as the return value for main().

    class phrases: #This is a class that stores all of the phrases needed for numbers in worded form.
        uno = { #Phrases used for the tens and ones positions in a number.
            1:"one",        2:"two",        3:"three",
            4:"four",       5:"five",       6:"six",
            7:"seven",      8:"eight",      9:"nine",
            10:"ten",       11:"eleven",    12:"twelve",
            13:"thirteen",  14:"fourteen",  15:"fifteen",
            16:"sixteen",   17:"seventeen", 18:"eighteen",
            19:"nineteen"
        }
        dos = { #Phrases used for values greater than twenty.
            2:"twenty",  3:"thirty",
            4:"fourty",  5:"fifty",
            6:"sixty",   7:"seventy",
            8:"eighty",  9:"ninety"
        }
        illion = [ #These are the prefixes of the "illions," like million, billion, trillion, etc.
            "m",      "b",      "tr",     "quad",
            "quint",  "sext",   "sept",   "oct",
            "non",    "dec",    "undec",  "duodec"
        ]

    for number in numbers: #Convert each number one after the other, and append each one to retval.
        retval += convert_num(number) + "\n" #The "\n" separates each result on different lines.

    return retval


numbers = argv[1:] #Getting the command line args.

parse_args()

#if "-v" in numbers or "--version" in numbers: #If args "-v" or "--version" are given, print the version number and exit.


try: #Checking if the args given are valid integers. Throw an error if one of them isn't.
    for num in numbers:
        num = int(num)
except ValueError:
    print("\033[1;31merror:\033[0m One of the args isn't an integer!",file=stderr)
    exit(2)
'''The values in numbers remain as strings after the checking code runs. I can't convert
them to ints, because large ints would get converted to word form incorrectly due to
floating point precision errors.'''

print(main(),end="")
