input()
s = list(map(int, input().split()))

idx = s.index(max(s))

print(sum(s[:idx]))
print(sum(s[idx+1:]))
