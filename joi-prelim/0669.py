x,l,r=map(int, input().split())
tmin = x
ti = l
for i in range(l,r+1):
	if tmin > abs(x-i):
		tmin = abs(x-i)
		ti = i
print(ti)
