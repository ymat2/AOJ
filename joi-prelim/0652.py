a,b,c = map(int, input().split())
coin_, day_ = 0, 0

while coin_ < c:
	day_ += 1
	coin_ += a
	if day_%7 == 0:
		coin_ += b

print(day_)
