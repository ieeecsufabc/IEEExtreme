def fib(n):
    if n<2 : return n
    elif not n in fib_dict :
        fib_dict[n]=fib(n-1) + fib(n-2)
    return fib_dict[n]
fib_dict = {}
output = []
t = input()
for x1 in xrange(t):
	num = input();
	output.append(str(fib(num+1)))
s = "\n"
print s.join(output)