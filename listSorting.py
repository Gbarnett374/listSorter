#!/usr/bin/python3 
import fileinput
import re

dict = {'numbers' : [], 'strings' : [], 'output' : [], 'key' : [] }

def hasNumber(line):
	global dict
	for string in line:
		is_num = False
		print(string)
		for char in string:
			if (char.isdigit()):
				is_num = True
				dict['key'].append('int')
				dict['numbers'].append(int(string))
				break
		if not is_num:
			dict['key'].append('string')
			dict['strings'].append(string)


line_array = []


for line in fileinput.input():
	print(line)
	# print (hasNumber(line))
	# hasNumber(line)
	# remove non-alphanumeric chars 
	re.sub(r'\W+', '', line)
	print(line);
	# strip line breaks from line.
	line = line.strip('\n')
	# create array of the strings in the line using ' ' as the delimiter
	line = line.split(' ')

	#Check if line has a numeric characters. 
	hasNumber(line)
	if not dict['numbers']: 
		print('array empty')
	else:
		dict['numbers'].sort()
		print(dict['numbers'])
	dict['strings'].sort()
	print(dict['strings'])

for item in dict['key']:
	if (item == 'int'):
		dict['output'].append(dict['numbers'][0])
		dict['numbers'].pop(0)

	else:
		dict['output'].append(dict['strings'][0])
		dict['strings'].pop(0)


print(dict['output'])


