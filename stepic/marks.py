with open('a.txt') as inf:
	with open('a.out', 'w') as outf:
		dm = [0, 0, 0]
		n = 0
		for line in inf:
			l = line.strip().split(';')
			print(l)
			outf.write(str((int(l[1]) + int(l[2]) + int(l[3])) / 3) + "\n")
			dm[0] += int(l[1])
			dm[1] += int(l[2])
			dm[2] += int(l[3])
			n += 1

		outf.write(str(dm[0] / n) + ' ' + str(dm[1] / n) + ' ' + str(dm[2] / n))
		