N = int(input())
S = input()

for i in range(N):
	if i-1>=0 and S[i] == "J":
		print(S[i-1])

