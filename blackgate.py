n = input()
arrays = []
name = []
number = []
saida = []
indexnumber = 0
x3 = 0
x4 = 1
for x1 in xrange(n):
	nome, numero = raw_input().split()
	arrays.append(numero+' '+nome)
arrays.sort()
for x2 in xrange(n):
	numero, nome = arrays[x2].split()
	number.append(numero)
	name.append(nome)
while indexnumber < n:
	valor = number.count(number[indexnumber])
	indexnumber = indexnumber + valor
	while x3 < indexnumber:
		saida.append(name[x3])
		x3 = x3 + 1
	while x4 <= indexnumber:
		saida.append(str(x4))
		saida.append(str(indexnumber))
		x4 = x4 + valor
	saida.append('\n')
saida.pop()
s = " "
print s.join(saida)