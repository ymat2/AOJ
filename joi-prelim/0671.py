input()
l = list(map(int, input().split()))

t = []
cnt = []
for i in l:
	if len(t) == 0:
		t.append(i)
	elif i >= t[-1]:
		t.append(i)
	else:
		cnt.append(len(t))
		t = []
		t.append(i)
cnt.append(len(t))
print(max(cnt))
