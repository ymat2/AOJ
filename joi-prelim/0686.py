import re

input()
s = input()


if re.search(r'.*I.*O.*I.*', s):
	print("Yes")
else:
	print("No")
