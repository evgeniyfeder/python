with open('a.txt') as inf:
	with open('a.out', 'w') as outf:
		line = inf.readline()
		i = 0
		while i < len(line):
			sym = line[i]
			num = 0
			i += 1
			while i < len(line) and '0' <= line[i] <= '9':
				num = 10 * num + int(line[i])
				i += 1
			for j in range(num):
				outf.write(sym)
			
