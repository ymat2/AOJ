input()
s = input()

def countox(string):
	l = len(string)
	i, cnt = 0, 0
	while i+2<=l:
		if string[i:i+2] == "OX" or string[i:i+2] == "XO":
			cnt += 1
			i += 2
		else:
			i += 1
	return cnt

print(countox(s))
