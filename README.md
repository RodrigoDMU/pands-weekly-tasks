# Higher Diploma in Science in Computing - Data Analytics
## Programming and Scripting (Weekly Tasks)

by: Rodrigo De Martino Ucedo

### Topic 1: Setting up the environment
*For this week task:*
- *Commit and push a file to the weekly tasks repository called helloworld.py. This file should contain a python program that displays Hello World when it is run.*
#### Program: helloworld.py
```

print("Hello World")

```
#### Comments:
The print() function prints the specified message to the screen, or other standard output.
### Topic 2: Statements 
*For this week task:*
- *Prompt the user and read in two money amounts (in cent).*
- *Add the two amounts.*
- *Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.*
- *Amount 01 = 65 and Amount 02 = 180.*
#### Program: bank.py
```
amount1 = int(input('Enter amount (in cent): '))
amount2 = int(input('Enter amount (in cent): '))
sum = amount1 / 100 + amount2 / 100
print(f'The sum of these is €{sum}')

```
#### Comments:
The input() function prompts the user to enter the values and int() convert the string into integer. The amounts were divided by 100 to convert cents into euros.
### Topic 3: Variables
*For this week task:*
- *Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).*
- *Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).*
#### Program: accounts.py
```
accountsno = str(input('Please enter an 10 digit account number: '))
print ('XXXXXX' + (accountsno[6:]))

```
#### Comments:
The input() function prompts the user to enter of 10 digit values and str() convert integers into string. The conversion to string was used to allow printing the replacement of numbers with the letter 'X' and "accountsno[6:]" was used to print only the numbers after the sixth number.
##### Extra:
*Modify the program to deal with account numbers of any length.*
```

accountsno2 = str(input('Please enter with your account number: '))
print (accountsno2.replace(accountsno2[:-4], "X"))

```
##### Coments:
I wrote a similar code to the requested in the accounts.py exercise using accountsno2 = str(input('Please enter with your account number: ')). When I wrote print, I used .replace to replace all numbers before the last 4 ([:-4]) with X.
### Topic 4: Controlling the flow
*For this week task:*
- *Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.*
- *At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.*
- *Have the program end if the current value is one.*
#### Program: collatz.py
```

goodinput = False
while not goodinput:
    try:
        number = int(input("Please enter a positive integer: "))
        if number > 0:
            goodinput = True
            print (number, end=" ")
        else:
            print ("That's not a positive number.")
    except ValueError:
        print ("That's not a positive number.") 
else:
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print (number, end=" ")
        else: 
            number = 3 * number +1
            print (number, end=" ")
    print (" ")

```
#### Comments:
While loop is a control flow statement that allows a block of code to be executed an indeterminate number of times, so long as the associated condition holds true. The first part of the programming ensures that only positive numbers will be insert (Stackoverflow reference). The second part is the programming to calculate the value where if the value is even, divide it by two, but if it is odd, multiply it by three and add one and the program end if the current value is one.

*'end=" "' was used to print the number on line in the next print() and print(" ") was used to print number on line without %.
#### References:
- Stackoverflow (https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer)
### Topic 5: Data
*For this week task:*
- *Write a program that outputs whether or not today is a weekday.*
- *An example of running this program on a Thursday is given below.*
    Yes, unfortunately today is a weekday.
- *An example of running it on a Saturday is as follows:*
    It is the weekend, yay!
#### Program: weekday.py
```
import datetime

today = datetime.datetime.today()

if today.weekday() <= 4:
    print ("Yes, unfortunately today is a weekday.")
else:
    today.weekday() == 5 or today.weekday() == 6
    print ("It is the weekend, yay!")

```
#### Comments:
This code imports the datetime module and retrieves today's date using datetime.datetime.today(). It then checks the day of the week using the today.weekday() method, which returns an integer from 0 (Monday) to 6 (Sunday).
#### Reference: 
- Shecodes (https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python)
### Topic 6: Functions
*For this week task:*
- *Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*
#### Program: squareroot.py