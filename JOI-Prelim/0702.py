N, K = list(map(int, input().split()))
S = input()
print("".join([j if i<K-1 else j.swapcase() for i,j in enumerate(S)]))
