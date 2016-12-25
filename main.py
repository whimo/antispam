# -*- coding: utf-8 -*-

import string

pairs = dict ()

def learn (sample_filename = "sample.txt"): 
	'''
		Learning method.
		Opens a file and learns its letter combinations
	'''

	with open (sample_filename) as sample:
		for word in sample:
			for i in range (len (word) - 1):
				pair = ''.join ([word [i + j].lower () for j in range (2)])
				
				if pair.isalpha ():
					add_pair (pair) # Add a two-letter combination



def add_pair (pair):
	'''
		Method for adding combinations into the dictionary
	'''

	if pair in pairs:
		pairs [pair] += 1

	else:
		pairs [pair] = 1


def rate (string):
	'''
		Method for rating a string
	'''

	rating = 1
	deg = 0 # Number of letter combinations in the input string

	for i in range (len (string) - 1):
		pair = (string [i] + string [i + 1]).lower ()
		
		
		if pair in pairs:
			deg += 1
			rating *= pairs [pair]

	return int (rating ** (1.0/deg)) # Geometric mean of letter combinations weights


def main ():
	learn ()

	string = str (input ())

	print ('String humanity index:', rate (string))
	

if __name__ == '__main__':
	main ()