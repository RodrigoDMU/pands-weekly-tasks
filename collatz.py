# Weekly Tasks 04

# Write a program, called collatz.py, that asks the user to input 
# any positive integer and outputs the successive 
# values of the following calculation.

# At each step calculate the next value by taking the 
# current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.

# Have the program end if the current value is one.

# Author: Rodrigo De Martino Ucedo

goodinput = False
while not goodinput:
    try:
        number = int(input("Please enter a positive integer: "))
        if number > 0:
            goodinput = True
            print (number, end=" ") # end=" " to print number on line
        else:
            print ("That's not a positive number.")
    except ValueError:
        print ("That's not a positive number.") 
else:
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print (number, end=" ") # end=" " to print number on line
        else: 
            number = 3 * number +1
            print (number, end=" ") # end=" " to print number on line
    print (" ") # " " to print number on line without %

    # Reference: Stackoverflow (https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer).
