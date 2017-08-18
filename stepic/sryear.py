with open('a.txt') as inf:
	l = [line.strip().split('\t') for line in inf]

v = [0 for i in range(11)]
cnt = [0 for i in range(11)]
for line in l:
	v[int(line[0]) - 1] += int(line[2])
	cnt[int(line[0]) - 1] += 1

with open('a.out', 'w') as outf:
	for i in range(11):
		if cnt[i] != 0:
			outf.write(str(i + 1) + ' ' + str(v[i] / cnt[i]) + '\n')
		else:
			outf.write(str(i + 1) + ' ' + '-\n')