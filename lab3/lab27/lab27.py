def read_lastnlines(fname,n):
	with open('lab27.txt') as f:
		for line in (f.readlines() [-n:]):
			print(line)

read_lastnlines('lab27.txt',1)