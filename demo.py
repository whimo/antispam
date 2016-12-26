# -*- coding: utf-8 -*-

import antispam, sys

def main ():
	
	print ('Enter filename of you sample text:')
	filename = str (input ())

	combs = antispam.learn (filename)

	print ('\nThe program has learned letter combinations of sample text.')
	print ('Now let\'s start.')


	while (True):
		print ('Enter the string you want to check (or "quit"):')
		string = str (input ())

		if string == 'quit':
			sys.exit ()

		print ('Humanity rating of your string:', antispam.rate (string, combs), '\n')


if __name__ == '__main__':
	main()
