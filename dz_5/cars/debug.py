# coding: utf-8
# module for cars db

import os


def wrong_input():
	print("Wrong parameter given. Please try again.")

def input_main():
	try:
		a = input("Choose action ([l]ist / [a]dd / [e]dit / [d]elete / [s]earch / [q]uit) ")
	except KeyboardInterrupt:
		print("\n Use [q] to quit!!!")
		a = "q"
	return a