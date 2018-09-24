#! /usr/bin/python3
# mapIt.py - Launches a map in the browser using an address from the command line clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get addres from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
