def is_selected(lst, slc):
	if len(slc) < 10:
		if len([j for j in slc if j[1]==lst[1]]) < 3:
			return True
		else:
			return False
	elif len(slc) < 20:
		if len([j for j in slc if j[1]==lst[1]]) < 2:
			return True
		else:
			return False
	elif len(slc) < 26:
		if len([j for j in slc if j[1]==lst[1]]) < 1:
			return True
		else:
			return False
	else:
		return False

while True:
	n = int(input())
	if n == 0:
		break
	else:
		slctd = []
		tms = [list(map(int, input().split())) for i in range(n)]
		tms = sorted(tms, key=lambda x: (-x[2], x[3], x[0]))
		for i in tms:
			if is_selected(i, slctd):
				slctd.append(i)
				print(i[0])

