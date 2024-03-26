# Higher Diploma in Science in Computing - Data Analytics
## Programming and Scripting (Weekly Tasks)

by: Rodrigo De Martino Ucedo

### Topic 1: Setting up the environment
*For this week task, commit and push a file to the weekly tasks repository called helloworld.py. This file should contain a python program that displays Hello World! when it is run.
#### Program: helloworld.py
```

print("Hello World")

```
### Topic 2: Statements 
*For this week task:
- Prompt the user and read in two money amounts (in cent)
- Add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
- Amount 01 = 65 and Amount 02 = 180
#### Program: bank.py
```
amount1 = int(input('Enter amount (in cent): '))
amount2 = int(input('Enter amount (in cent): '))
sum = amount1 / 100 + amount2 / 100
print(f'The sum of these is €{sum}')
```
#### Comments:
The input() function prompts the user to enter the values and int() convert the string to integer.