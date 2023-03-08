def sum_hit(i):
	x=0
	for j in range(int(i)):
		x += int(input())
		# x += y
	return x

while True:
	n=int(input())
	if n == 0:
		break
	else:
		print(sum_hit(n/4))

"""
while True:
    n=int(input())
    if n == 0:
        break
    else:
        print(sum([int(input()) for i in range(int(n/4))]))
"""
