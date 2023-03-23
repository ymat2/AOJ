n,m = map(int, input().split())
a = list(map(int, input().split()))
print(max([a.count(j+1) for j in range(m)]))
