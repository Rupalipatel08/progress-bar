import sys

def one(args):
	sys.stderr.write('%d/r'  %args)

for n in range(1000):
	one(n)
