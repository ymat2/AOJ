input()
m = list(map(int, input().split(" ")))
n = list(map(int, input().split(" ")))

for i in sorted(list(set(m))):
	if i in n:
		print(i)

""" refactored by cahtGPT
input()
m = set(map(int, input().split()))
n = set(map(int, input().split()))
for i in sorted(m.intersection(n)):
    print(i)
"""
