# Weekly Tasks 03

# Write a python program called accounts.py 
# that reads in a 10 character account number 
# and outputs the account number with only the
# last 4 digits showing 
# (and the first 6 digits replaced with Xs).

# Author: Rodrigo De Martino Ucedo

accountsno = str(input('Please enter an 10 digit account number: '))
print ('XXXXXX' + (accountsno[6:]))


# Extra:

accountsno2 = str(input('Please enter with your account number: '))
print (accountsno2.replace(accountsno2[:-4], "X"))

# I wrote similar code to the requested in the accounts.py exercise, 
# using accountsno2 = str(input('Please enter with your account number: ')). 
# When I wrote print, I used .replace to replace all numbers before 
# the last 4 with X.