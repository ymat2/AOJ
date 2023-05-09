input()
pos = list(map(int, input().split()))
input()
tm = list(map(int, input().split()))

def try_move(j,lst):
	if lst[j-1]+1 not in set(lst) and lst[j-1] < 2019:
		lst[j-1] = lst[j-1] + 1

for i in tm:
	try_move(i, pos)

for k in pos:
	print(k)
