with open("a.txt") as inf:
	with open("a.out", "w") as outf:
		d = dict()
		for line in inf:
			for word in [i.lower() for i in line.split()]:
				if word in d:
					d[word] += 1
				else:
					d[word] = 1

		max_ind = 0
		max_v = 0
		for k, v in d.items():
			if v > max_v:
				max_ind = k
				max_v = v

		outf.write(max_ind + " " + str(d[max_ind])) 		