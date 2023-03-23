l = list(map(int, input().split()))
print(sum([max(l)-i for i in l]))
