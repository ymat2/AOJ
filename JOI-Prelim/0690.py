input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def jcount(n, lst):
	l = [j for j in lst if j>=n]
	return len(l)

m = sum([jcount(i, b) for i in a])
print(m)
