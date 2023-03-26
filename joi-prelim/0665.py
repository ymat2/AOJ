n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

while len(A) > 0 and len(B) > 0:
	if A[0] <= B[0]:
		print(A[0])
		del A[0]
	else:
		print(B[0])
		del B[0]

if len(A) > 0:
	for i in A:
		print(i)
else:
	for i in B:
		print(i)
