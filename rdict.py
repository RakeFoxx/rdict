#!/usr/bin/env python3

# TODO: support for derivative words

import json

datafile = 'rdict.json'

# reads json file 'datafile' into 'jdict' list
def parse():
	global jdict
	df = open(datafile)
	raw = df.read()
	df.close()
	jdict = json.loads(raw)

# recursively adds lines of formatted 'val' to 'outlist'
def _fstr(val, outlist, offstr = '', tabstr = ' ' * 4):
	if type(val) == dict:
		for k, v in val.items():
			outlist.append('{}{}:'.format(offstr, k))
			_fstr(v, outlist, offstr + tabstr, tabstr)
	elif type(val) == list:
		if len(val) == 1:
			_fstr(val[0], outlist, offstr, tabstr)
		else:
			for i in range(len(val)):
				outlist.append('{}({})'.format(offstr, i + 1))
				_fstr(val[i], outlist, offstr + tabstr, tabstr)
	else:
		outlist.append('{}{}'.format(offstr, val))

# returns the formatted string for 'val'
def fstr(val):
	l = []
	_fstr(val, l)
	return '\n'.join(l); # no additional ending '\n'

# returns formatted word definition for w
def define(w):
	# linear search
	global jdict
	val = [x for x in jdict if x['word'] == w][0]
	return fstr(val)

# cli dictionary when run directly
def main():
	parse()
	while True:
		print("Enter a word:")
		w = input()
		print(define(w))

if __name__ == '__main__':
	main()
