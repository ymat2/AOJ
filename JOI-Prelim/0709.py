N = input()
S = list(input().strip())  # delete white spaces from both ends

if len(set(S)) >= 3:
	print("Yes")
else:
	print("No")

# why WA???
