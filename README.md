# Antispam
***A very simple antispam-like app written in pure python, without any external libraries.***

When learning, the algorythm analyzes letter combinations in sample text.
When processing a string, the algorythm compares letter combinations and rates it.

The sample text should be saved with UTF-8 encoding.

It is preferable to use Python3 because it has better unicode support.


Here is an example of using the program to analyze a string (learnt on "David Copperfield"):
```
whimo@wml:~/Documents/antispam$ python3 demo.py
Enter filename of you sample text:
sample.txt

The program has learned letter combinations of sample text.
Now let's start.
Enter the string you want to check (or "quit"):
The first rule of the Fight Club: you don't talk about Fight Club.
Humanity rating of your string: 542

Enter the string you want to check (or "quit"):
HRsfknv spb sfibn aeoSdfbn sodj.
Humanity rating of your string: 1
```
