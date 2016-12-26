# -*- coding: utf-8 -*-

import string

def learn (sample_filename = "sample.txt", comb_len = 3):
	'''
		Learning method.
		Opens a file and learns its letter combinations

		sample_filename: filename of the sample text, should be saved with UTF-8
		comb_len: letter combination length
	'''

	combs = dict ()

	with open (sample_filename) as sample:
		for word in sample:
			for i in range (len (word) - comb_len + 1):
				comb = ''.join ([word [i + j].lower () for j in range (comb_len)])
				
				if comb.isalpha ():
					add_comb (comb, combs) # Add a letter combination

	return (combs)




def add_comb (comb, combs):
	'''
		Method for adding combinations into the dictionary
	'''

	if comb in combs:
		combs [comb] += 1

	else:
		combs [comb] = 1

	return combs


def rate (string, combs):
	'''
		Method for rating a string
	'''

	rating = 1
	deg = 0 # Number of letter combinations in the input string

	comb_len = len (list (combs.keys ()) [0])

	for i in range (len (string) - comb_len + 1):
		comb = ''.join ([string [i + j].lower () for j in range (comb_len)])

		if comb.isalpha ():
			deg += 1
		
		if comb in combs:
			rating *= combs [comb]


	if deg == 0:
		return 0

	return int (rating ** (1.0/deg)) # Geometric mean of letter combinations weights
