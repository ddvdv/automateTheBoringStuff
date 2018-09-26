#! /home/davidv/.virtualenvs/automateBS/bin/python

import os, docx

def throwInvite(guestsFile):
	guestList = open(guestsFile, 'r')
	for line in guestList.readlines():
		print('this is: ' + line)


throwInvite('guests.txt')
