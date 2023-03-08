input()
N = list(map(int, input().split(" ")))

j = [10000000, ""]
for i in sorted(list(set(N))):
	if N.count(i) < j[0]:
		j = [N.count(i), i]
print(j[1])
