# Write a program that outputs whether or not today is a weekday. 
# (The program should be called weekday.py)
# You will need to search the web to find how you work out what day it is.
# An example of running this program on a Thursday is given below.

# $ python weekday.py
# Yes, unfortunately today is a weekday.

# An example of running it on a Saturday is as follows:

# $ python weekday.py
# It is the weekend, yay!

# Author: Rodrigo De Martino Ucedo


import datetime

today = datetime.datetime.today()

if today.weekday() <= 4:
    print ("Yes, unfortunately today is a weekday.")
else:
    today.weekday() == 5 or today.weekday() == 6
    print ("It is the weekend, yay!")



# This code imports the datetime module and retrieves today's 
# date using datetime.datetime.today(). 
# It then checks the day of the week using the today.weekday() method, 
# which returns an integer from 0 (Monday) to 6 (Sunday).
# Reference: Shecodes