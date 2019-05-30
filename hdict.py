#!/usr/bin/env python3
datafile = '/Users/zero/Desktop/F4T Dictionary/rdict/hdict.data'
tdict = {}

def parse():
	global tdict
	for line in open(datafile):
		l = line.split(':')
		tdict[l[0]] = l[1].strip()

def define(w):
	global jdict
	nf_msg = '<span style="color:red">Sorry! Word not found.</span>'
	if w in tdict:
		r = ''
		for i, s in enumerate(tdict[w].split(','), start = 1):
			r += f'{i:>3}. {s}<br/>'
		return r
	else:
		return nf_msg

# cli dictionary when run directly
def main():
	parse()
	while True:
		print("Enter a word:")
		w = input()
		print(define(w))

if __name__ == '__main__':
	main()