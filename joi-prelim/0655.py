input()
japan = list(map(int, input().split()))
levels = set(japan+[0])

def as01(i):
	if i>0:
		return 1
	else:
		return 0

def count01(lst):
	lst2str = list(map(str, lst))
	return "".join(lst2str).count("01")

def how_many_islands(level_):
	list_ = [i-level_ for i in japan]
	list_ = list(map(as01, list_))
	if list_[0] == 0:
		return count01(list_)
	else:
		return count01(list_)+1

def count_island(level_):
	cnt, island = 0, 0
	list_ = [i-level_ for i in japan]
	for i in list_:
		if island == 0 and i > 0:
			cnt += 1
			island = 1
		elif island == 0 and i <= 0:
			continue
		elif island == 1 and i > 0:
			continue
		else:
			island = 0
	return cnt

def count_island_(level_):
	cnt, island = 0, 0
	prev = -1
	for i in japan:
		if i >= level_ and prev < 0:
			cnt += 1
		prev = i - level_
	return cnt

#print(max([count_island(japan, l) for l in levels]))
print(max(list(map(count_island_, levels))))
