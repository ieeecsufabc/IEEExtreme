t = input()
output = []
armas = []
firepower = []
peso = []
x3 = 0
for x1 in xrange(t):
	exit = 0
	totalarmas = 0
	c, n = map(int, raw_input().split())
	for x2 in xrange(n):
		w, f = map(int, raw_input().split())
		armas.append(str(f) + ' ' + str(w))
	armas.sort()
	armas.reverse()
	for x2 in xrange(n):
		p1, p2 = armas[x2].split()
		firepower.append(p1)
		peso.append(p2)
	while x3 < n:	
		if peso[x3] == c:
			totalarmas = totalarmas + firepower[x3]
			exit = 1
		elif peso[x3] < c:
			totalarmas = totalarmas + firepower[x3]
			c = c - peso[x3]
		x3 = x3 + 1
	output.append(str(totalarmas))
s = "\n"
print s.join(output)