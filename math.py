def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))
t = input()
output = []
for x1 in xrange(t):
	a, b, c = map(int, raw_input().split())
	if a != 1:
		b1 = factorial(b)
		c1 = factorial(c)
		bc1 = factorial(b-c)
		final = b1/(c1*bc1) 
		final = a ** final
		final = final % 1000000007
		output.append(str(final))
	else:
		output.append('1')
s = "\n"
print s.join(output)