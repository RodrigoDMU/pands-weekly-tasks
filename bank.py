# Weekly Tasks 02

# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Amount 01 = 65 and Amount 02 = 180

# Author Rodrigo De Martino Ucedo

amount1 = int(input('Enter amount (in cent): '))
amount2 = int(input('Enter amount (in cent): '))
sum = amount1 / 100 + amount2 / 100
print(f'The sum of these is €{sum}')