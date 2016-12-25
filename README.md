# Antispam
A very simple antispam based on machine learning and written in python.

When learning, the algorythm analyzes letter combinations in sample text.
When processing a string, the algorythm compares letter combinations and rates it.

The sample text should be saved with UTF-8 encoding.

```
whimo@wml:~/Documents/antispam$ python3 main.py
The first rule of the Fight Club: you don't talk about Fight Club.
String humanity index: 4109

whimo@wml:~/Documents/antispam$ python3 main.py
HRsfknv spb sfibn aeoSdfbn sodj
String humanity index: 200
```
