[n,m] = list(map(int, input().split(" ")))

ii = [[str(i+1)] for i in range(n)]

def move_ball(i, j, lst):
	for sblst in lst:
		if str(i) in sblst:
			sblst.remove(str(i))
	lst[j-1].append(str(i))

def get_pos(n, lst):
	for sblst in lst:
		if n in sblst:
			return lst.index(sblst)

for k in range(m):
	[i,j] = list(map(int, input().split(" ")))
	move_ball(i,j,ii)

# print(ii)

for k in range(n):
	print(get_pos(str(k+1), ii)+1)
