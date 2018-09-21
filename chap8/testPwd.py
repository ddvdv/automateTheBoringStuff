#! python3

import re


longEnough = re.compile(r'.{8}')
upper = re.compile(r'[A-Z]')  # one upper and one lower
lower = re.compile(r'[a-z]')  # one upper and one lower
oneDigit = re.compile(r'\d') # at least one digit

def strongTest(pwd):
   if longEnough.search(pwd) and upper.search(pwd) and lower.search(pwd) and oneDigit.search(pwd):
        return True
   else:
        return False

def main():
    pwdToTest = input('Please enter your password: ')
    if strongTest(pwdToTest):
       print('yo passwoord is goood man')
    else:
       print('your password is weak, and so is your soul.')
       main()

main()
