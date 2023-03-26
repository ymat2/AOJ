n = int(input())
l = [n]
while n > 0:
	n -= 1
	if n+sum([int(i) for i in str(n)]) in set(l):
		l.append(n)
print(len(l))
