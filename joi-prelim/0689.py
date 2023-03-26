n = int(input())
s = input()

cnt = 0
for i in range(n):
	if i%2 == 0:
		if s[i] != "I":
			cnt += 1
	else:
		if s[i] != "O":
			cnt += 1
print(cnt)

"""use enumerate()

cnt = 0
for i, c in enumerate(s):
    if (i % 2 == 0 and c != "I") or (i % 2 == 1 and c != "O"):
        cnt += 1

"""
