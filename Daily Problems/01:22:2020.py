#A program to generate a list of safe passwords
import random

#A secure password has a combination of: 
#mix of lowercase letters, uppercase letters, numbers, and symbols.
ValidChars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*?!'
passwords = []
#A function to generate the requested amount of passwords
def GeneratePasswords(n):
    if n >= 0:
        tmppass = "".join(random.sample(ValidChars, random.randint(8,15)))
        print(tmppass)
        passwords.append(tmppass)
        GeneratePasswords(n - 1)
    
#asking the user for the amount of passwords they would like to generate?
generations = input('How many password would you like to generate? ')
GeneratePasswords(int(generations))

#make sure the password is from the list
while True:
    newPassword = input('Enter the password you\'d like to use: ')
    if newPassword in passwords:
        break
    else:
        print('That password is not from the valid passwords list. Please choose a valid password')

#ask for login
while True:
    enteredPass = input('Enter the password again to sign in: ')

    if newPassword == enteredPass:
        print('You have successfully signed in!')
        break
    else:
        print('The password is incorrect')
