n = int(input())
l = {n}  # 集合しか勝たん

while n > 0:
	n -= 1
	if n+sum([int(i) for i in str(n)]) in l:
		l.add(n)
print(len(l))

