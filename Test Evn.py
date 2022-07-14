from difflib import Differ

print('''
Welcome to the File Compartor Section.
---Code Meaning---
‘-‘ line unique to sequence 1
‘+’ line unique to sequence 2
‘ 'line common to both sequences
‘?’ line not present in either input sequence
---Code Meaning---

DON'T FORGET TO ADD .txt TO THE FILE IN ORDER FOR IT TO WORK
''')

FILEONE = input('File 1 ...: ')
FILETWO = input('File 2 ...: ')

with open(FILEONE) as file_1, open(FILETWO) as file_2:
	differ = Differ()


	for line in differ.compare(file_1.readlines(), file_2.readlines()):
		print(line)



